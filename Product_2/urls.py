from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [  
   path('product_2',views.product_2),
   path('product_2_data/<int:id>',views.product_2_data)
]
