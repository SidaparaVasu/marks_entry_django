from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse 
from superadmin.models import Institute, Course
from superadmin.forms import InstituteForm, CourseForm

# Create your views here.
def indexDashboard(request):
    return render(request, "index.html")

def profile(request):
    return render(request, "profile.html")


# Institute CRUD starts here
def institute(request):
    context ={"Institute":Institute.objects.all()}   
    return render(request,'institute.html',context)  

def addInstitute(request):
    if request.method == "POST":     
        form = InstituteForm(request.POST or None) 
        if form.is_valid():   
            form.save()
            messages.success(request, "Institute added successfully!")
            return redirect("/superadmin/institute") 
        else:
            messages.error(request, "Insertion failed!")
        return redirect("/superadmin/institute")
    else:  
        form = InstituteForm()  
    return redirect("/superadmin/institute",{'form':form})

# Request UpdateInstitute Page
def updateInstitute(request,id):
    context = Institute.objects.get(id=id)
    return render(request, "updateInstitute.html",{'context' : context})

# Update Function Of Institute
def editInstitute(request,id):
    context = {}
    obj = get_object_or_404(Institute, id=id)
    form = InstituteForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("/superadmin/institute")

    context['form'] = form
    return render(request, "institute.html",context)

def deleteInstitute(request,id):
    context ={}
    obj = get_object_or_404(Institute,id=id)
    if request.method == "GET":
        obj.delete()
        return redirect("/superadmin/institute")
    return render(request,'institute.html',context)
# Institute CRUD ends here


# Course CRUD starts here
def course(request):
    context ={"Course":Course.objects.all()}   
    return render(request,'course.html',context)  

def addCourse(request):
    if request.method == "POST":     
        form = CourseForm(request.POST or None) 
        if form.is_valid():   
            form.save()
            messages.error(request, "Course added successfully!")
            return redirect("/superadmin/course") 
        else:
            messages.error(request, "Insertion failed!")
        return redirect("/superadmin/course")
    else:  
        form = CourseForm()  
    return redirect("/superadmin/course",{'form':form})

# Request UpdateCourse Page
def updateCourse(request,id):
    context = Course.objects.get(id=id)
    return render(request, "updateCourse.html",{'context' : context})

# Update Function Of Course
def editCourse(request,id):
    context = {}
    obj = get_object_or_404(Course, id=id)
    form = CourseForm(request.POST or None, instance=obj)

    if form.is_valid():
        if form.save():
            messages.success(request, "Course updation successfully!")
        else:
            messages.error(request, "Course updation failed!")
        return redirect("/superadmin/course")

    context['form'] = form
    return render(request, "course.html",context)

def deleteCourse(request,id):
    context ={}
    obj = get_object_or_404(Course,id=id)
    if request.method == "GET":
        obj.delete()
        return redirect("/superadmin/course")
    return render(request,'course.html',context)
# Course CRUD ends hereCourseForm
