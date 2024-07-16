from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   path('employee',views.employee),
   path('employeeform',views.employeeform),
   path('deletedata/<int:id>',views.deletedata),  
   path('updateemployeedata/<int:id>',views.updateemployeedata), 
]