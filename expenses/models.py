from django.utils import timezone
from django.db import models

# Create your models here.
class ExpenseCategory(models.Model):
    name = models.CharField(max_length=50)
    description= models.CharField(max_length=180, blank=True, default='none')

    def __str__(self):
        return f'{self.name}'

class Expense(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=180, blank=True, default='none')
    amount = models.CharField(max_length=100)
    category = models.ForeignKey(to=ExpenseCategory, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name} | {self.price} | {self.amount}'