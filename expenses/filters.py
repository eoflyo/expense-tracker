from .models import Expense
import django_filters

class ExpenseFilter(django_filters.FilterSet):
    class Meta:
        model = Expense
        fields = ['category', 'date']