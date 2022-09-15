from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from auth_app.forms import RegisterForm  
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
from . models import users


#
import logging,traceback
logger = logging.getLogger('django')
#


# Create your views here.
def loginPage(request):
    return render(request, 'login.html')

def registerPage(request):
    return render(request, 'register.html')

def registration(request):
    if request.method == "POST":     
        form = RegisterForm(request.POST or None)  
        if form.is_valid():  
            form.save()  
            messages.success(request, "You are registered sucessfully in as {username}!")
            return render(request,'login.html')  
        else:
            messages.error(request, "Registration failed! {username}!")
    else:  
        form = RegisterForm()  
    return render(request,'register.html',{'form':form})  

def loginHandle(request):
    if request.method == "POST":    
        form = RegisterForm(request.POST)
        un = request.POST.get("username")
        ps = request.POST.get("password")

        flag = 0
        data = users.objects.all()
        for i in range(len(data)):
            if data[i].username == un and data[i].password == ps:
                if data[i].type == 1:
                    logger.info("super admin: " + data[i].username + " is logged in")
                    return HttpResponseRedirect('/superadmin')
                elif data[i].type == 2:
                    logger.info("admin: " + data[i].username + " is logged in")
                    return HttpResponseRedirect('/administrator')
                elif data[i].type == 3:
                    logger.info("faculty: " + data[i].username + " is logged in")
                    return HttpResponseRedirect('/faculty')
            else:
                flag = 1
        if flag == 1:
            html = "Invaild Credentials! Please try again!" + "<a href='login'>Go back</a>"
            return HttpResponse(html)
    else:
        form = RegisterForm()
        return render(request, template_name = "login.html", context = {"form":form})

def logoutHandle(request):
    if request.method == "POST":    
        logout(request)
        messages.success(request, "Successfully Logged Out!")
        return redirect("/")