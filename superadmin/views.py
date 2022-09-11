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
        if form.is_valid():   
            form.save()
            messages.error(request, "Institute added successfully!")
            return redirect("/superadmin/institute")
            #return render(request,'institute.html')  
        else:
            messages.error(request, "Insertion failed!")
            return render(request,'institute.html')  
    else:  
        form = InstituteForm()  
    return render(request,'institute.html',{'form':form})

def showInstitute(request):
    context = {"Institute":Institute.objects.all()}
    return render(request,'institute.html',context)  
    
def deleteInstitute(request,id):
    context ={}
    obj = get_object_or_404(Institute,id=id)
    if request.method == "GET":
        obj.delete()
        return redirect("/superadmin/institute")
    return render(request,'institute.html',context)

#Request UpdateInstitute Page
def updateInstitute(request,id):
    context = Institute.objects.get(id=id)
    return render(request, "updateInstitute.html",{'context' : context})

#Update Function Of Institute
def editInstitute(request,id):
    context = {}
    obj = get_object_or_404(Institute, id=id)
    form = InstituteForm(request.POST or None, instance=obj)

    if form.is_valid():
        #return HttpResponse(form)
        form.save()
        return redirect("/superadmin/institute")

    context['form'] = form
    return render(request, "institute.html",context)