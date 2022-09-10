from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse 
from superadmin.models import Course, Institute
from superadmin.forms import InstituteForm, CourseForm

# Create your views here.
def indexDashboard(request):
    return render(request, "index.html")

def profile(request):
    return render(request, "profile.html")

def institute(request):
    context = Institute.objects.all()
    return render(request,'institute.html',{'Institute':context})  

def course(request):
    # return render(request, "course.html")
    context = Course.objects.all()
    return render(request,'course.html',{'Course':context}) 

# Institute CRUD starts   
def addInstitute(request):
    if request.method == "POST":     
        form = InstituteForm(request.POST or None) 
        if form.is_valid():   
            form.save()
            messages.success(request, "Institute added successfully!")
            return redirect("/superadmin/institute")
            #return render(request,'institute.html')  
        else:
            messages.error(request, "Insertion failed!")
            return render(request,'institute.html')  
    else:  
        form = InstituteForm()  
    return render(request,'institute.html',{'form':form})
 

def deleteInstitute(request,id):
    context ={}
    obj = get_object_or_404(Institute,id=id)
    if request.method == "GET":
        obj.delete()
        messages.error(request, "Institute Deleted Succesfully!")
        return redirect("/superadmin/institute")
    return render(request,'institute.html',context)

# Institute CRUD ends

# Course CRUD starts
def addCourse(request):
    if request.method == "POST":     
        form = CourseForm(request.POST or None) 
        if form.is_valid():  
            form.save()
            messages.success(request, "Course added successfully!")
            return redirect("/superadmin/course")
        else:
            messages.error(request, "Insertion failed!")
            return redirect("/superadmin/course") 
    else:  
        form = CourseForm()  
    return render(request,'course.html',{'form':form})

def deleteCourse(request,id):
    context ={}
    obj = get_object_or_404(Course,id=id)
    if request.method == "GET":
        obj.delete()
        messages.error(request, "Course Deleted Succesfully!")
        return redirect("/superadmin/course")
    return render(request,'course.html',context)
# Course CRUD ends
