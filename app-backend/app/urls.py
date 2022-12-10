"""app URL Configuration"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounting/ping', views.ping, name='ping'),
    path('api/accounting/accounts', views.AccountListView.as_view()),
    path('api/accounting/accounts/<account_id>', views.AccountDetailsView.as_view()),
    path('api/accounting/transactions', views.TransactionListView.as_view()),
    path('api/accounting/transactions/<transaction_id>', views.TransactionDetailsView.as_view())
]
