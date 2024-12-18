# Ex02 Django ORM Web Application
## Date: 18/12/2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import BankLoan, BankLoanAdmin


if not admin.site.is_registered(BankLoan):
    admin.site.register(BankLoan, BankLoanAdmin)


models.py

from django.db import models
from django.contrib import admin
class BankLoan(models.Model):
    loan_id = models.IntegerField(primary_key=True)
    loan_type = models.CharField(max_length=30)
    loan_amt = models.IntegerField()
    cust_name = models.CharField(max_length=30)
    cust_acno = models.IntegerField()

    def __str__(self):
        return f"Loan ID: {self.loan_id}, Customer: {self.cust_name}"

class BankLoanAdmin(admin.ModelAdmin):
    list_display = ('loan_id', 'loan_type', 'loan_amt', 'cust_name', 'cust_acno')
admin.site.register(BankLoan, BankLoanAdmin)


```


## OUTPUT
![Screenshot (27)](https://github.com/user-attachments/assets/781638c3-aaf9-436b-8404-33d5c8fa2da0)
![er](https://github.com/user-attachments/assets/2cd6d1ee-7fe1-4bfd-b800-07aafc40c056)





## RESULT
Thus the program for creating a database using ORM hass been executed successfully
