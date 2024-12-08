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
