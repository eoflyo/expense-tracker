from lib2to3.fixes.fix_input import context
from django.shortcuts import render
from expenses.models import Expense, ExpenseCategory
from expenses.forms import AddExpenseForm, AddCategoryForm

def index(request):
    context = {
        'title': 'Ваши траты',
        'expenses': Expense.objects.all(),
        'categories': ExpenseCategory.objects.all(),
    }
    return render(request, 'expenses/index.html', context)

def expenses(request):
    category_form = AddCategoryForm(prefix='category_form')
    expense_form = AddExpenseForm(prefix='expense_form')
    if request.method == 'POST':
        if 'expense_form' in request.POST:
            expense_form = AddExpenseForm(data=request.POST, prefix='expense_form')
            expense = Expense()
            expense.name = request.POST['name']
            expense.amount = request.POST['amount']
            expense.price = request.POST['price']
            expense.category = ExpenseCategory.objects.get(id=request.POST['category'])
            expense.description = request.POST['description']
            expense.save()
            category_form = AddCategoryForm(prefix='category_form')

        elif 'category_form' in request.POST:
            category_form = AddCategoryForm(data=request.POST, prefix='category_form')
            category = ExpenseCategory()
            category.name = request.POST['name']
            category.description = request.POST['description']
            category.save()
            expense_form = AddExpenseForm( prefix='expense_form')
    else:
        expense_form = AddExpenseForm(prefix='expense_form')
        category_form = AddCategoryForm(prefix='category_form')
    context = {
        'title': 'Список трат',
        'expenses': Expense.objects.all(),
        'categories': ExpenseCategory.objects.all(),
        'category_form': category_form,
        'expense_form': expense_form,
    }
    return render(request, 'expenses/expenses.html', context)