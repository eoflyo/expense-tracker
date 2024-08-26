from django.urls import path
from expenses.views import index, expenses

app_name = 'expenses'

urlpatterns = [
    path('expenses/', expenses, name='expenses'),
    path('', index, name='index')
]