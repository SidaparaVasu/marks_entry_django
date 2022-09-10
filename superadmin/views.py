from django.shortcuts import render,redirect,get_object_or_404
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
            return redirect("/superadmin/institute")
            #return render(request,'institute.html')  
        else:
            messages.error(request, "Registration failed! {username}!")
    else:  
        form = InstituteForm()  
    return render(request,'register.html',{'form':form})

def showInstitute(request):
    context ={"Institute":Institute.objects.all()}
   
    return render(request,'institute.html',context)  
    
def deleteInstitute(request,id):
    context ={}
    obj = get_object_or_404(Institute,id=id)
    if request.method == "GET":
        obj.delete()
        return redirect("/superadmin/institute")
    return render(request,'institute.html',context)
