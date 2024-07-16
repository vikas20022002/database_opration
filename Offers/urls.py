from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   path('offers',views.offers),
   path('offersform',views.offersform),
   path('deleteoffers/<int:id>',views.deleteoffers),
   path('updateoffersdata/<int:id>',views.updateoffersdata),
   path('addofferusingform',views.addofferusingform),
]