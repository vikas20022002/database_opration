from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from datetime import datetime
from .models import CouponModel
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
# Create your views here.

def coupondata (request):
    return render(request,"coupon.html")
        
    # else:
    #     my_date = request.POST.get("validity")
    #     d = datetime.strptime(my_date, "%m/%d/%Y")
    #     obj = CouponModel()
    #     obj.coupon_title = request.POST.get("coupontitle")
    #     obj.coupon_code = request.POST.get("couponcode")
    #     obj.coupon_date = d.strftime("%Y-%m-%d")  
    #     obj.coupon_noofuse = request.POST.get("nouse")
    #     obj.coupon_active = request.POST.get("couponactive")
    #     obj.coupon_description = request.POST.get("coupondescription")
    #     obj.save()
    #     messages.success(request, 'Data inserted successfully!')
    # return redirect('/coupon')

@csrf_exempt
def insertCoupon(request):
    my_date = request.POST.get("validity")
    d = datetime.strptime(my_date, "%d-%m-%Y")
    couponid = request.POST.get("couponid")
    message=""
    if len(couponid) == 0:
        obj = CouponModel()
        message = "Record inserted successfully"
    else:
        message = "Record Updated successfully"
        obj = CouponModel.objects.filter(coupon_id=couponid).get()
    obj.coupon_title = request.POST.get("coupontitle")
    obj.coupon_code = request.POST.get("couponcode")
    obj. coupon_date = d.strftime("%Y-%m-%d")  
    obj.coupon_noofuse = request.POST.get("nouse")
    obj.coupon_active = request.POST.get("couponactive")
    obj.coupon_description = request.POST.get("coupondescription")
    obj.save()
    return HttpResponse(message)

def getCouponData(request):
    data = CouponModel.objects.all()
    allcoupon = list(data.values())
    #allcoupon = serialize('json',data)
    return JsonResponse(allcoupon,safe=False)
    
@csrf_exempt
def deleteCouponData(request):
    deleteid = request.POST.get("deleteid")
    CouponModel.objects.filter(coupon_id=deleteid).delete()
    return HttpResponse("Delete Successfully")
@csrf_exempt
def getSingleCouponData(request):
    editid = request.POST.get("editid")
    data = CouponModel.objects.filter(coupon_id=editid)
    coupon = list(data.values())
    return JsonResponse(coupon,safe=False)