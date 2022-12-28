"""app URL Configuration"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounting/ping', views.ping, name='ping'),
    path('api/v1/results', views.ResultListView.as_view(), name="get_result_list"),
    path('api/v1/createresult', views.ResultCreateView.as_view(), name="create_result")
]
