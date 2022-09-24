from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from auth_app.models import users
from auth_app.forms import RegisterForm
from superadmin.models import Course
from superadmin.forms import CourseForm
from .models import Batch
from .forms import BatchForm

# Create your views here.
def adminIndex(request):
    return render(request, 'index_admin.html')

# Admin CRUD starts 
def faculty(request):
    context ={"faculty":users.objects.all().filter(type="3")}
    return render(request,'faculty.html',context)

def addFaculty(request):
    if request.method == "POST":     
        form = RegisterForm(request.POST or None, request.FILES)  
        if len(request.FILES) != 0:
            form.image = request.FILES['image']  
        if form.is_valid():  
            form.save()  
            messages.success(request, "Faculty added successfully!")
            return redirect("/administrator/faculty")  
        else:
            messages.error(request, "Error in registration for faculty!")
    else:  
        form = RegisterForm()  
    return redirect("/administrator/faculty",{'form':form})

# Request Update faculty Page
def updateFaculty(request,id):
    context = users.objects.get(id=id)
    return render(request, "updateFaculty.html",{'context' : context})

# Update Function Of faculty
def editFaculty(request,id):
    context = {}
    obj = get_object_or_404(users, id=id)
    form = RegisterForm(request.POST or None, instance=obj)

    if form.is_valid():
        if form.save():
            messages.success(request, "Faculty data updation successfully!")
        else:
            messages.error(request, "Faculty data updation failed!")
        return redirect("/administrator/faculty")
    else:
        messages.error(request, "Form is not valid! please fill up form currectly!")
    context['form'] = form
    return redirect("/administrator/faculty", context)

def deleteFaculty(request,id):
    context ={}
    obj = get_object_or_404(users,id=id)
    if request.method == "GET":
        if obj.delete():
            messages.success(request,"Data deleted successfully for Id : " + str(id))
            return redirect("/administrator/faculty")
        else:
            messages.error(request," deletion failed for Id : " + str(id))
    return redirect("/administrator/faculty", context)
# Admin CRUD ends here

#BATCH CRUD starts

def batch(request):
    context = {'Batch':Batch.objects.all().select_related('courseName'),'Courses':Course.objects.all()}
    return render(request,'batch.html',context)

def addBatch(request):
    if request.method == "POST":     
        form = BatchForm(request.POST or None)  
        if form.is_valid():  
            form.save()  
            messages.success(request, "Batch added successfully!")
            return redirect("/administrator/batch")
            #return render(request,'admin.html')  
        else:
            messages.error(request, "Error in registration for batch!")
    else:  
        form = BatchForm()  
    return redirect("/administrator/batch",{'form':form})
#