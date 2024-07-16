from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.

def checklogin(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        em = request.POST.get("loginEmail")
        pwd = request.POST.get("loginPassword")
        user = authenticate(username=em,password=pwd)
        if user is not None:
            login(request,user) #session
            return redirect("/")
        else:
            messages.error(request, "Email or password not found")
            return render(request, 'login.html')



def registration(request):
    if request.method == "GET":
        return render(request,'registration.html')
    else:
        # user = User.objects.create(first_name = request.POST.get("first_name"),username =request.POST.get("username"),email=request.POST.get("email"))
        if User.objects.filter(email=request.POST.get("email")).exists():
            messages.error(request, "A user with this email already exists.")
            return render(request, 'registration.html')
        

        user = User.objects.create(
            first_name=request.POST.get("first_name"),
            
            username=request.POST.get("email"),
            email=request.POST.get("email"),
        )
        user.set_password(request.POST.get("password1"))
        user.save()

        messages.success(request, "Registration successful. You can now log in.")
        return redirect("/login")
    
def userlogout(request):
    logout(request)
    return redirect("/login")


# def changpassword(request):
#     if request.method == "GET":          
#         return render(request,"changepassword.html")
#     else:
#         #chanhge 
#         pass

def changpassword(request):
    if request.method == "POST":
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')

        if not request.user.check_password(current_password):
            messages.error(request, 'Current password is incorrect.')
            return redirect('/changpassword')
        else:
            user = request.user
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/changpassword')
    else:
        return render(request,"changepassword.html")