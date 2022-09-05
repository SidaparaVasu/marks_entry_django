from django.shortcuts import render
from django.contrib import messages

from superadmin.forms import AddInstitute  


# Create your views here.
def indexDashboard(request):
    return render(request, "index.html")

def profile(request):
    return render(request, "profile.html")

def institute(request):
    return render(request, "institute.html")

def addInstitue(request):
    if request.method == "POST":     
        form = AddInstitute(request.POST or None)  
        if form.is_valid():  
            form.save()  
            messages.success(request, "You are registered sucessfully in as {username}!")
            return render(request,'login.html')  
        else:
            messages.error(request, "Registration failed! {username}!")
    else:  
        form = AddInstitute()  
    return render(request,'register.html',{'form':form})