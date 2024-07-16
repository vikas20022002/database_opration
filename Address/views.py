from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .models import AddressModel
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def address(request):    
    return render(request,'address.html')
    
@csrf_exempt
def addaddressdata(request):
    obj = AddressModel()
    obj.address_title = request.POST.get('addtitle')
    obj.address_line_1 = request.POST.get('addline1')
    obj.address_line_2 = request.POST.get('addline2')
    obj.address_city = request.POST.get('addcity')
    obj.address_state = request.POST.get('addstate')
    obj.address_type = request.POST.get('addtype')
    obj.save()
    return HttpResponse("Record inserted successfully")


def getaddresdata(request):
    data = AddressModel.objects.all()
    alldata = list(data.values())
    return JsonResponse(alldata,safe=False)

@csrf_exempt
def deleteaddress(request):
    deleteid = request.POST.get("deleteid")
    AddressModel.objects.filter(address_id=deleteid).delete()
    return HttpResponse("Delete Successfully")