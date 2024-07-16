from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import CityModel
from State.models import StateModel
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import os
from django.conf import settings

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def city(request):
    data = CityModel.objects.all
    context = {
        "citydata" : data
    }
    return render(request,'city.html',context)  

def cityform(request):
    if request.method == "GET":
        data = StateModel.objects.all
        context = {
            "statedata" : data
        }
        return render(request,'addcitydata.html',context)
    else:
        #image upload
        cityimage = request.FILES['cityimg']
        fs=FileSystemStorage()
        file = fs.save(cityimage.name,cityimage)
        fileurl = fs.url(file)   
        
        obj = CityModel()
        obj.city_name = request.POST.get("cityname")
        obj.city_img = fileurl
        stateobj = StateModel.objects.filter(state_id = request.POST.get("stateid")).get()
        obj.state_id = stateobj
        obj.save()
        messages.success(request, 'Data inserted successfully!')
        return redirect('/cityform')
    
def citydelete(request,id):
    obj = CityModel.objects.filter(city_id=id).get()
    imagpath =  obj.city_img
    image_name = os.path.basename(imagpath)
    os.remove(os.path.join(settings.MEDIA_ROOT,image_name))
    CityModel.objects.filter(city_id=id).delete()
    messages.success(request, 'Data Delete successfully!')
    return redirect('/city') 

def cityupdate(request,id):
    if request.method == "GET":
        data =  CityModel.objects.filter(city_id=id).get()
        context = {
            "citydata" : data
        }
        return render(request,"updatecityfprm.html",context)

    else:
        obj = CityModel.objects.filter(city_id=id).get()

        if request.FILES.get('cityimg') is not None:
        # old img
            imagpath =  obj.city_img
            image_name = os.path.basename(imagpath)
            os.remove(os.path.join(settings.MEDIA_ROOT,image_name))
        # new img update
            cityimage = request.FILES['cityimg']
            fs=FileSystemStorage()
            file = fs.save(cityimage.name,cityimage)
            fileurl = fs.url(file)
            obj.city_img = fileurl  

        obj.city_name = request.POST.get("cityname")
        obj.save()
        messages.success(request, 'Data updated successfully!')
        return redirect('/city')    
@csrf_exempt   
def citybystate(request):
    stateid = request.POST.get("stateid")
    data = CityModel.objects.filter(state_id=stateid)
    city = list(data.values())
    return JsonResponse(city,safe=False)