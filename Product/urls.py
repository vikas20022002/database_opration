from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   path('product',views.product),
   path('productform',views.productform),
   path('deleteproduct/<int:id>',views.deleteproduct),
   path('updateproductdata/<int:id>',views.updateproductdata),
]