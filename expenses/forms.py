import datetime
from django import forms
from django.utils import timezone

from .models import Expense, ExpenseCategory

class AddExpenseForm(forms.ModelForm):
    CHOICES = (
        ('Option 2', 'Январь'),
        ('Option 2', 'Февраль'),
        ('Option 2', 'Март'),
        ('Option 2', 'Апрель'),
        ('Option 2', 'Май'),
        ('Option 2', 'Июнь'),
        ('Option 2', 'Июль'),
        ('Option 2', 'Август'),
        ('Option 2', 'Сентябрь'),
        ('Option 2', 'Октябрь'),
        ('Option 2', 'Ноябрь'),
        ('Option 2', 'Декабрь'),
    )

    name = forms.CharField(widget=forms.TextInput(attrs={'class' :"form-control", 'placeholder' : "Названиe"}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class' :"form-control", 'placeholder' : "Описание"}), required=False)
    amount = forms.CharField(widget=forms.NumberInput(attrs={'class' :"form-control", 'placeholder' : "200"}), initial=1)
    category = forms.ModelChoiceField(queryset=ExpenseCategory.objects.all(), widget=forms.Select( attrs={'class' :"form-control"} ))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class' :"form-control", 'placeholder' : "2000"}))
    month = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control", 'placeholder': "Месяц"}), choices=CHOICES, initial='Option 2', required=True)
    week = forms.IntegerField(widget=forms.NumberInput(attrs={'class' :"form-control", 'placeholder' : "1"}), required=True)


    class Meta:
        model = Expense
        fields = ('name', 'description', 'amount', 'category', 'price')

class AddCategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' :"form-control", 'placeholder' : "Названиe"}), max_length=50)
    description = forms.CharField(widget=forms.TextInput(attrs={'class' :"form-control", 'placeholder' : "Описание"}),max_length=180, required=False)

    class Meta:
        model = ExpenseCategory
        fields = ('name', 'description')