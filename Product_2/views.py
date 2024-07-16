from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import productmodel_2
# Create your views here.

def product_2(request):
    data = productmodel_2.objects.all
    context = {
        "productData_2":data
    }
    return render(request,'product-2.html',context)

def product_2_data(request,id):     
    data = productmodel_2.objects.filter(product_2_id = id).get()
    context = {
                "productData_2":data 
    }        
    return render(request,'product_2_data.html',context)