from django.contrib import admin
from .models import Account, Transaction, Choice, Category, Result, Guest

admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Choice)
admin.site.register(Category)
admin.site.register(Result)
admin.site.register(Guest)