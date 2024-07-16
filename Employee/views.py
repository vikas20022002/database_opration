from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib import messages
from .models import EmployeeModel
from City.models import CityModel
from State.models import StateModel
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
# Create your views here.

def employee(request):
    data = EmployeeModel.objects.all
    context = {
        "employeedata":data
    }
    return render(request,'employee.html',context)

def employeeform(request):
    if request.method == "GET" :
        statedata = StateModel.objects.all
        context = {
            "statedata" : statedata,
    }
        return render(request,'employeeform.html',context)
    else :
        #image upload
        catimage = request.FILES['pho-1']
        fs=FileSystemStorage()
        file = fs.save(catimage.name,catimage)
        fileurl = fs.url(file)

        obj = EmployeeModel()
        obj.employee_name = request.POST.get("textname")
        obj.employee_photo_id = fileurl
        obj.employee_salary = request.POST.get("textsalary")
        obj.employee_gender = request.POST.get("textgender")
        obj.employee_department = request.POST.get("textdepartment")
        cityobj = CityModel.objects.filter(city_id = request.POST.get("cityid")).get()
        obj.city_id =cityobj
        obj.save()
        messages.success(request, 'Data inserted successfully!')
        return redirect('/employeeform')
    
    
def deletedata(request,id):
    obj =  EmployeeModel.objects.filter(employee_id=id).get()   
    imgepath = obj.employee_photo_id
    image_name = os.path.basename(imgepath)
    os.remove(os.path.join(settings.MEDIA_ROOT,image_name))    
    EmployeeModel.objects.filter(employee_id=id).delete()
    messages.success(request, 'Data Deleted successfully!')
    return redirect('/employee')



def updateemployeedata(request,id):
    if request.method == "GET":
        data =EmployeeModel.objects.filter(employee_id=id).get()
        context = {
            "employeedata":data,
            "citydata": CityModel.objects.all()
        }
        return render(request,'updateemployeedata.html',context)
    else:
        obj = EmployeeModel.objects.filter(employee_id=id).get()

        if request.FILES.get('pho1') is not None:
            #Old image Delete+
            imgepath = obj.employee_photo_id
            image_name = os.path.basename(imgepath)
            os.remove(os.path.join(settings.MEDIA_ROOT,image_name))
            #new Image upload
            catimage = request.FILES['pho1']
            fs=FileSystemStorage()
            file = fs.save(catimage.name,catimage)
            fileurl = fs.url(file) 
            obj.employee_photo_id = fileurl

        obj.employee_name = request.POST.get("textname") 
        obj.employee_salary = request.POST.get("textsalary")
        obj.employee_gender = request.POST.get("textgender")
        obj.employee_department = request.POST.get("textdepartment")
        cityobj = CityModel.objects.filter(city_id = request.POST.get("cityid")).get()
        obj.city_id =cityobj

        obj.save()
        messages.success(request, 'Data Updated successfully!')
        return redirect('/employee')