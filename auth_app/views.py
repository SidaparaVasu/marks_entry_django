from django.shortcuts import render, HttpResponse
from auth_app.forms import RegisterForm  
from django.contrib import messages
#from auth_app.models import users
from . import models

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
            messages.error(request, "Registration failed! due to less Aukat of {username}!")
    else:  
        form = RegisterForm()  
    return render(request,'register.html',{'form':form})  