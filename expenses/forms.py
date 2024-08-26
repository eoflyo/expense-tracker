from email.policy import default

from django import forms
from .models import Expense, ExpenseCategory


class AddExpenseForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=180)
    amount = forms.CharField(max_length=100)
    category = forms.ModelChoiceField(queryset=ExpenseCategory.objects.all())
    price = forms.IntegerField()

    class Meta:
        model = Expense
        fields = ('name', 'description', 'amount', 'category', 'price')

class AddCategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=180)

    class Meta:
        model = ExpenseCategory
        fields = ('name', 'description')