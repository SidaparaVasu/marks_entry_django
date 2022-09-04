from django.shortcuts import render, HttpResponse
from auth_app.forms import RegisterForm  
#from auth_app.models import users
from . import models

# Create your views here.
def login(request):
    return render(request, 'login.html')

def faculty_register(request):
    return render(request, 'register.html')

def registration(request):
    if request.method == "POST":     
        form = RegisterForm(request.POST or None)  
        #return HttpResponse(form)
        if form.is_valid():  
            try:  
                print("Hello")
                form.save()  
                return render(request,'login.html')  
            except:  
                pass  
    else:  
        form = RegisterForm()  
    return render(request,'register.html',{'form':form})  