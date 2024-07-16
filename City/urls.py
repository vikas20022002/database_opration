from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('city',views.city),
    path('cityform',views.cityform),
    path('citydelete/<int:id>',views.citydelete),
    path('cityupdate/<int:id>',views.cityupdate), 
    path('citybystate',views.citybystate),   
]