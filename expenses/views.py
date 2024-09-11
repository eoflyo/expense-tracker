from django.shortcuts import render
from .models import Expense, ExpenseCategory
from .forms import AddExpenseForm, AddCategoryForm
from django.db.models import Case, Sum, When
from django.db import models
from django.http import HttpResponseRedirect

FIRST_WEEK = 1
SECOND_WEEK = 2
THIRD_WEEK = 3
FOURTH_WEEK = 4

WEEKS = {
    'first': 1,
    'second': 2,
    'third': 3,
    'fourth': 4,
}

def totals_by_category(categories, month='September'):
    aggregation_expression = {}
    data = {}
    for category in categories:
        field_name = category.name
        aggregation_expression[field_name] = Sum(
            Case(When(category=category, then='price'),
                 default=0,
                 output_field=models.DecimalField())
        )
    for week in WEEKS:
        data[week] = Expense.objects.filter(week=WEEKS[week], month=month).aggregate(**aggregation_expression)
        data[week]['Сумма'] = Expense.objects.filter(week=WEEKS[week], month=month).aggregate(Sum('price'))['price__sum']
    return data

def index(request):
    context = {
        'title': 'Ваши траты',
        'expenses': Expense.objects.all(),
        'categories': ExpenseCategory.objects.all(),
        'totals' : totals_by_category(ExpenseCategory.objects.all(), 'August'),
    }
    return render(request, 'expenses/index.html', context)

def expenses(request):
    expenses = Expense.objects.all()

    if request.method == 'POST':
        expense_form = AddExpenseForm(data=request.POST)
        expense = Expense()
        expense.name = request.POST['name']
        expense.amount = request.POST['amount']
        expense.price = request.POST['price']
        expense.category = ExpenseCategory.objects.get(id=request.POST['category'])
        expense.description = request.POST['description']
        expense.month = request.POST['month']
        expense.week = request.POST['week']
        expense.save()
    else:
        expense_form = AddExpenseForm(data=request.POST)

    context = {
        'title': 'Список трат',
        'expenses': expenses,
        'categories': ExpenseCategory.objects.all(),
        'expense_form': expense_form,
    }
    return render(request, 'expenses/expenses.html', context)

def category_form(request):
    if request.method == 'POST':
        category_form = AddCategoryForm(data=request.POST)
        category = ExpenseCategory()
        category.name = request.POST['name']
        category.description = request.POST['description']
        category.save()
    else:
        category_form = AddCategoryForm(data=request.POST)

    context = {
        'title': 'Список трат',
        'category_form': category_form,
        'categories': ExpenseCategory.objects.all(),
    }

    return render(request, 'expenses/category.html', context)

def delete_expense(request, id):
    expense = Expense.objects.get(id=id)
    expense.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])