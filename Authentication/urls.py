from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   path('login',views.checklogin),
   path('registration',views.registration),  
   path('logout',views.userlogout),
   path('changpassword',views.changpassword),
]