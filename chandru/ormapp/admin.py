from django.contrib import admin
from .models import BankLoan, BankLoanAdmin

# Check if the model is already registered before registering it again
if not admin.site.is_registered(BankLoan):
    admin.site.register(BankLoan, BankLoanAdmin)
