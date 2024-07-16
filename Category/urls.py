from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   path('category',views.category),
   path('categoryform',views.categoryform),
   path('categorydelete/<int:id>',views.categorydelete),     
   path('updatecategorydata/<int:id>',views.updatecategorydata), 
]