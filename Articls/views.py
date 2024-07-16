from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib import messages
from .models import AricalModel

# Create your views here.
def articls (request):
    data = AricalModel.objects.all
    context = {
        'articaldata':data
    }
    return render(request,"articls.html",context)


def articlsform (request):
    if request.method == "GET" :
      return render(request,"articlsform.html")
    else :
       obj = AricalModel()
       obj.artical_title = request.POST.get("artitle")
       obj.artical_description = request.POST.get("ardescription")
       obj.artical_active = request.POST.get("aractive")
       obj.artical_authors = request.POST.get("arauthors")
       obj.artical_date = request.POST.get("ardate")
       obj.artical_quote = request.POST.get("arquote")
       obj.save()
       messages.success(request, 'Data inserted successfully!')
    return redirect('/articlsform')


def articaldelete(request,id):
    AricalModel.objects.filter(artical_id = id).delete()
    messages.success(request, 'Data deleted successfully!')
    return redirect('/articls')



def updatearticlsdata(request,id):
   if request.method == "GET":
      data = AricalModel.objects.filter(artical_id = id).get()
      context = {
      "articaldata": data
      }
      return render(request,"updatearticlsdata.html",context)
   else:
      obj = AricalModel.objects.filter(artical_id = id).get()
      obj.artical_title = request.POST.get("artitle")
      obj.artical_description = request.POST.get("ardescription")
      obj.artical_active = request.POST.get("aractive")
      obj.artical_authors = request.POST.get("arauthors")
      obj.artical_date = request.POST.get("ardate")
      obj.artical_quote = request.POST.get("arquote")
      obj.save()
      messages.success(request, 'Data updated successfully!')
      return redirect('/articls')
