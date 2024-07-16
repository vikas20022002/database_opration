from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib import messages
from .models import OffersModel
from .forms import OfferForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/login")
def offers(request):
    data = OffersModel.objects.all
    context = {
        "offerdata":data
    }    
    return render(request,'offers.html',context)

def offersform(request):
    # if request.method == "GET":
    #    return render(request,'offersform.html')
    # else:
    #     obj = OffersModel()
    #     obj.offer_name = request.POST.get('ofname')
    #     obj.offer_description = request.POST.get('ofdescription')
    #     obj.offer_maxvalue = request.POST.get('ofmax')
    #     obj.offer_minvalue = request.POST.get('ofmin')
    #     obj.offer_discount = request.POST.get('ofdis')
    #     obj.save()

    if request.method == "GET":
        return render(request,'offersform.html')
    else:
        form = OfferForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data inserted successfully!')
            return redirect('/offersform')
    
def deleteoffers(request,id):
    OffersModel.objects.filter(offer_id=id).delete()
    messages.success(request, 'Data Delete successfully!')
    return redirect('/offers')




def updateoffersdata(request,id):
    if request.method == "GET":
        data = OffersModel.objects.filter(offer_id=id).get()
        context = {
        "offerdata":data
        }   
        return render(request,'updateoffersdata.html',context)
    else:
        obj = OffersModel.objects.filter(offer_id=id).get()
        obj.offer_name = request.POST.get('ofname')
        obj.offer_description = request.POST.get('ofdescription')
        obj.offer_maxvalue = request.POST.get('ofmax')
        obj.offer_minvalue = request.POST.get('ofmin')
        obj.offer_discount = request.POST.get('ofdis')
        obj.save()
        
        messages.success(request, 'Data updated successfully!')
        return redirect('/offers')


def addofferusingform(request):
    if request.method == "GET":
        context = {
            "form": OfferForm()
        }
        return render(request,'addofferusingform.html',context)
    else:
       form = OfferForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request, 'Data added successfully!')
           return redirect('/offers')