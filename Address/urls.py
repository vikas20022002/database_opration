from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('address',views.address),
    path('addaddressdata',views.addaddressdata),
    path('getaddresdata',views.getaddresdata),
    path('deleteaddress',views.deleteaddress),
]