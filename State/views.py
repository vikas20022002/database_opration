from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import StateModel
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import os
from django.conf import settings

# Create your views here.

def state(request):
    data = StateModel.objects.all
    context = {
        "statedata" : data
    }
    return render(request,'state.html',context)


def addstatedata(request):
    if request.method == "GET":
        return render(request,"addstatedata.html")
    else:
        #image upload
        stateimge = request.FILES['stateimg']
        fs = FileSystemStorage()
        file = fs.save(stateimge.name,stateimge)
        fileurl = fs.url(file)

        obj = StateModel()
        obj.state_name = request.POST.get('statename')
        obj.state_img = fileurl
        obj.save()
        messages.success(request,"Data inserted successfully!")
        return redirect('/addstatedata')
    
def deletestatedata(request,id):
    obj = StateModel.objects.filter(state_id = id).get()
    imgpath = obj.state_img
    image_name = os.path.basename(imgpath)
    os.remove(os.path.join(settings.MEDIA_ROOT,image_name))
    StateModel.objects.filter(state_id = id).delete()
    messages.success(request,"Data Deleted succeddfully!")
    return redirect('/state')

def updatestatedata(request,id):
    if request.method == "GET":
        data = StateModel.objects.filter(state_id = id).get()
        context = {
            "statedata" : data
        }
        return render(request,"updatestatedata.html",context)
    else:
        obj = StateModel.objects.filter(state_id = id).get()

        if request.FILES.get('stateimg') is not None:
        # old img
            imgpath = obj.state_img
            image_name = os.path.basename(imgpath)
            os.remove(os.path.join(settings.MEDIA_ROOT,image_name))
        # new img
            stateimge = request.FILES['stateimg']
            fs = FileSystemStorage()
            file = fs.save(stateimge.name,stateimge)
            fileurl = fs.url(file)
            obj.state_img = fileurl


        obj.state_name = request.POST.get('statename')
        obj.save()
        messages.success(request,"Data updated succeddfully!")
    return redirect('/state')
            