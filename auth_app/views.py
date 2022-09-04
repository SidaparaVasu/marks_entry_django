from django.shortcuts import render, redirect, get_object_or_404
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
        
        if form.is_valid():
            loginusername = form.cleaned_data.get('username')
            loginpassword =  form.cleaned_data.get('password')
        
            # obj = get_object_or_404(users, username=loginusername)
            # res = check_password(loginpassword,obj.password1)
            user = authenticate(username=loginusername, password=loginpassword)
            
            if user == True:
                messages.info(request, "You are now logged in as {loginusername}")
                return redirect("/")
        else:
            messages.error(request, "Invalid credential! Please try again")
            return redirect("loginPage")
    else:
        form = RegisterForm()
        return render(request, template_name = "login.html", context = {"form":form})

def logoutHandle(request):
    if request.method == "POST":    
        logout(request)
        messages.success(request, "Successfully Logged Out!")
        return redirect("/")