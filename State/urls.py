from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('state',views.state),
    path('addstatedata',views.addstatedata),
    path('deletestatedata/<int:id>',views.deletestatedata),
    path('updatestatedata/<int:id>',views.updatestatedata)    
]