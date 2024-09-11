from django.urls import path
from .views import index, expenses, category_form, delete_expense

app_name = 'expenses'

urlpatterns = [
    path('expenses/', expenses, name='expenses'),
    path('', index, name='index'),
    path('delete_expense/<int:id>/', delete_expense, name='delete_expense'),
    path('categories/', category_form, name='categories')
]