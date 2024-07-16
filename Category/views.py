from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import CategoryModel
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
# Create your views here.

def category(request):
    data = CategoryModel.objects.all
    context = {
        "categorydata" : data
    }
    return render(request,'category.html',context)

def categoryform(request):
    if request.method == "GET" :        
        return render(request,'categoryform.html')
    else :

        category_name = request.POST.get("coname")
        catimage = request.FILES['coimg']

        # Check for duplicates
        if CategoryModel.objects.filter(category_name=category_name).exists():
            messages.error(request, "A category with this name already exists.")
            return redirect('/categoryform')
        
        # Check for duplicate image
        fs = FileSystemStorage()
        file = fs.save(catimage.name, catimage)
        fileurl = fs.url(file)

        # Save the new category
        obj = CategoryModel()
        obj.category_name = category_name
        obj.category_img = fileurl
        obj.save()

        
        messages.success(request, 'Data inserted successfully!')
        return redirect('/category')
        
        # #image upload
        # catimage = request.FILES['coimg']
        # fs=FileSystemStorage()
        # file = fs.save(catimage.name,catimage)
        # fileurl = fs.url(file)   
        
        # obj = CategoryModel()
        # obj.category_name = request.POST.get("coname")
        # obj.category_img = fileurl
        # obj.save()
        # messages.success(request, 'Data inserted successfully!')
        # return redirect('/categoryform')


def categorydelete(request,id):
    #image delete
    obj = CategoryModel.objects.filter(category_id=id).get()
    imagepath = obj.category_img
    image_name = os.path.basename(imagepath)
    os.remove(os.path.join(settings.MEDIA_ROOT,image_name))
    #Record Delete
    CategoryModel.objects.filter(category_id=id).delete()
    messages.success(request, 'Data Delete successfully!')
    return redirect('/category')



def updatecategorydata(request,id):
    if request.method == "GET":
        data = CategoryModel.objects.filter(category_id=id).get()
        context = {
        "categorydata" : data
        }
        return render(request,'updatecategorydata.html',context)

    else:
        obj = CategoryModel.objects.filter(category_id=id).get()

        if request.FILES.get('coimg') is not None:
            #Old image Delete+
            imagepath = obj.category_img
            image_name = os.path.basename(imagepath)
            os.remove(os.path.join(settings.MEDIA_ROOT,image_name))
            #new Image upload
            catimage = request.FILES['coimg']
            fs=FileSystemStorage()
            file = fs.save(catimage.name,catimage)
            fileurl = fs.url(file) 
            obj.category_img = fileurl 

        obj.category_name = request.POST.get("coname")
        obj.save()
        messages.success(request, 'Data updated successfully!')
        return redirect('/category')