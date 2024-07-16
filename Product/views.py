from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib import messages
from .models import ProductModel
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
# Create your views here.

def product(request):
    data = ProductModel.objects.all
    context = {
        "productData":data
    }
    return render(request,'product.html',context)

def productform(request):
    if request.method == "GET":
        return render(request,'productform.html')
    else:
        #image upload
        proimage = request.FILES['img1']
        fs1=FileSystemStorage()
        file1 = fs1.save(proimage.name,proimage)
        fileurl1 = fs1.url(file1)
        

        proimage = request.FILES['img2']
        fs2=FileSystemStorage()
        file2 = fs2.save(proimage.name,proimage)
        fileurl2 = fs2.url(file2)

        obj = ProductModel()
        obj.product_name = request.POST.get("txtname")
        obj.product_qty = request.POST.get("txtqty")
        obj.product_img1 = fileurl1
        obj.product_img2 = fileurl2
        obj.product_price = request.POST.get('txtprice')
        obj.product_description = request.POST.get("txtdescription")
        obj.save()
        messages.success(request, 'Data inserted successfully!')
        return redirect('/productform')

def deleteproduct(request,id):
    obj =  ProductModel.objects.filter(product_id = id).get()
    imgepath1 = obj.product_img1
    image_name1 = os.path.basename(imgepath1)
    os.remove(os.path.join(settings.MEDIA_ROOT,image_name1))

    imgepath2 = obj.product_img2
    image_name2 = os.path.basename(imgepath2)
    os.remove(os.path.join(settings.MEDIA_ROOT,image_name2))

    ProductModel.objects.filter(product_id = id).delete()
    messages.success(request, 'Data deleted successfully!')
    return redirect('/product')

def updateproductdata(request,id):
    if request.method == "GET":
        data = ProductModel.objects.filter(product_id = id).get()
        context = {
        "productdata":data
        }
        return render(request,"updateproductform.html",context)
    else:
        obj=ProductModel.objects.filter(product_id = id).get()

        if request.FILES.get('img1') is not None:

            #Old image Delete+

            imgepath1 = obj.product_img1
            image_name1 = os.path.basename(imgepath1)
            os.remove(os.path.join(settings.MEDIA_ROOT,image_name1))

            #new Image upload

            proimage = request.FILES['img1']
            fs1=FileSystemStorage()
            file1 = fs1.save(proimage.name,proimage)
            fileurl1 = fs1.url(file1)
            obj.product_img1 = fileurl1

        if request.FILES.get('img2') is not None:

            #Old image Delete+

            imgepath2 = obj.product_img2
            image_name2 = os.path.basename(imgepath2)
            os.remove(os.path.join(settings.MEDIA_ROOT,image_name2))

            #new Image upload

            proimage = request.FILES['img2']
            fs2=FileSystemStorage()
            file2 = fs2.save(proimage.name,proimage)
            fileurl2 = fs2.url(file2) 
            obj.product_img2 = fileurl2      


        obj.product_name = request.POST.get("txtname")
        obj.product_qty = request.POST.get("txtqty")
        obj.product_price = request.POST.get('txtprice')
        obj.product_description = request.POST.get("txtdescription")
        obj.save()
        messages.success(request, 'Data updated successfully!')
        return redirect('/product')
