from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Shopping', 'Shopping'),
        ('Other', 'Other'),
        
    ]

    amount = models.IntegerField()
    category = models.CharField(max_length=20,
   choices = CATEGORY_CHOICES)
    note = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.category} - {self.amount}"
    
