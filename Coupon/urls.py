from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   path('coupon',views.coupondata),
   path('insertCoupon',views.insertCoupon),
   path('getCouponData',views.getCouponData),
   path('deleteCouponData',views.deleteCouponData),  
   path('getSingleCouponData',views.getSingleCouponData),  
]