from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse 
from superadmin.models import Institute
from superadmin.forms import InstituteForm

# Create your views here.
def indexDashboard(request):
    return render(request, "index.html")

def profile(request):
    return render(request, "profile.html")

def institute(request):
    context ={"Institute":Institute.objects.all()}
   
    return render(request,'institute.html',context)  
    
def addInstitute(request):
    if request.method == "POST":     
        form = InstituteForm(request.POST or None) 
        #return HttpResponse(form) 
        if form.is_valid():  
            form.save()  
            messages.success(request, "You are registered sucessfully in as {username}!")
            return render(request,'institute.html')  
        else:
            messages.error(request, "Registration failed! {username}!")
    else:  
        form = InstituteForm()  
    return render(request,'register.html',{'form':form})

def showInstitute(request):
    context ={"Institute":Institute.objects.all()}
   
    return render(request,'institute.html',context)  
    