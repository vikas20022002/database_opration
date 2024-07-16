from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('articls',views.articls),
    path('articlsform',views.articlsform),
    path('articaldelete/<int:id>',views.articaldelete),
    path('updatearticlsdata/<int:id>',views.updatearticlsdata),
]