from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from auth_app.forms import RegisterForm  
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import check_password
from . models import users
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
        uname = users.objects.all().filter(username=un)
        
       
        if uname[0].username == un and uname[0].password == ps:
            return HttpResponse('successful')
        
    else:
        form = RegisterForm()
        return render(request, template_name = "login.html", context = {"form":form})

def logoutHandle(request):
    if request.method == "POST":    
        logout(request)
        messages.success(request, "Successfully Logged Out!")
        return redirect("/")