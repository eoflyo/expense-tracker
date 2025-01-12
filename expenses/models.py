from django.utils import timezone
from django.db import models


# Create your models here.
class ExpenseCategory(models.Model):
    name = models.CharField(max_length=50)
    description= models.CharField(max_length=180)

    def __str__(self):
        return f'{self.name}'

class Expense(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=180, default='', blank=True)
    amount = models.CharField(max_length=100)
    category = models.CharField(max_length=180)
    price = models.PositiveIntegerField(default=0)
    week = models.PositiveIntegerField(default=1)
    month = models.CharField(max_length=32, default='August')

    def __str__(self):
        return f'{self.name} | {self.price} | {self.amount}'