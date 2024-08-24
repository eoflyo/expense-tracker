from lib2to3.fixes.fix_input import context
from django.shortcuts import render
from expenses.models import Expense, ExpenseCategory
from expenses.forms import AddExpenseForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    context = {
        'title': 'Ваши траты',
        'expenses': Expense.objects.all(),
        'categories': ExpenseCategory.objects.all(),
    }
    return render(request, 'expenses/index.html', context)

def expenses(request):
    context = {
        'title': 'Список трат',
        'expenses': Expense.objects.all(),
        'categories': ExpenseCategory.objects.all(),
    }
    return render(request, 'expenses/expenses.html', context)

def add_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = AddExpenseForm(request.POST)
        expense.name = form['name']
        expense.amount = form['amount']
        expense.price = form['price']
        expense.category = form['category']
        expense.description = form['description']
        expense.date = expense['date']
        expense.save()
    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expenses/expenses.html', context)