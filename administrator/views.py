from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from auth_app.models import users
from auth_app.forms import RegisterForm
from superadmin.models import Course
from superadmin.forms import CourseForm
from .models import Batch,Semester,Subject,Student
from .forms import BatchForm,SemesterForm,SubjectForm,StudentForm
from django.db.models import Count, Max
from django.http import JsonResponse
from django.views.generic import View
# from django.views.decorators.csrf import csrf_exempt

# logger
import logging,traceback
logger = logging.getLogger('superadminLogger')
#

# Create your views here.
def adminIndex(request):
    return render(request, 'index_admin.html')

# Admin CRUD starts 
def faculty(request):
    faculty = users.objects.all().filter(type="3")
    p = Paginator(faculty, 10)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except Paginator.PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except Paginator.EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context ={'page_obj': page_obj} 
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

# BATCH CRUD starts
def batch(request):
    Batches = Batch.objects.all().select_related('courseName')
    p = Paginator(Batches, 10)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except Paginator.PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except Paginator.EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context ={'page_obj': page_obj}
    return render(request,'batch.html', context)

def addBatch(request):
    if request.method == "POST":     
        form = BatchForm(request.POST or None) 
        if form.is_valid():  
            form.save()  
            messages.success(request, "Batch added successfully!")
            return redirect("/administrator/batch")
        else:
            messages.error(request, "Error in registration for batch!")
    else:  
        form = BatchForm()  
    return redirect("/administrator/batch",{'form':form})
    # return HttpResponse("404 Page not Found!")
# Batch CRUD ends here

# SEMESTER CRUD STARTS
def semester(request):
    context = {
        'Semesters': Semester.objects.values('courseName').annotate(tot_sems=Count('semester')),
        'Courses': Course.objects.all() 
    }
    return render(request,'semester.html', context) 

def addSemester(request):
    if request.method == "POST":     
        form = SemesterForm(request.POST or None)  
        if form.is_valid():  
            form.save()  
            messages.success(request, "Semester added successfully!")
            return redirect("/administrator/semester")
            #return render(request,'admin.html')  
        else:
            messages.error(request, "Error in registration for Semester!")
    else:  
        form = BatchForm()  
    return redirect("/administrator/Semester",{'form':form})

def updateSemester(request,id):
    context = Semester.objects.get(id=id)
    return render(request, "updateSemester.html",{'context' : context})
# SEMESTER CRUD ends here


# Subject crud starts

# def subject(request):
#     context = {
#         'courses':Course.objects.all(),
#         'subjects':Subject.objects.all().select_related('semester'),
#     }
#     return render(request,'subject.html',context)

# def fetch_semesters(request, course_id, course_name):
# @csrf_exempt
def subject(request):
    if request.method == "POST":
        course_id = request.POST.get('dropdown-courseid')
        context = {
            'courses': Course.objects.all(),
            'semesters': Semester.objects.all().filter(courseName_id=course_id),
            'selected_course': [course_id],
            'subjects':Subject.objects.all().select_related('semester'),
        }
        print(course_id)
        return render(request,'subject.html',context)
    else: 
        course_id = 0
        context = {
            'courses': Course.objects.all(),
            'semesters': Semester.objects.all().filter(courseName_id=course_id),
            'selected_course': [course_id],
            'subjects':Subject.objects.all().select_related('semester'),
        }
        return render(request,'subject.html',context)  

def addSubject(request):
    if request.method == "POST":             
        form = SubjectForm(request.POST or None)  
        if form.is_valid():  
            form.save()  
            messages.success(request, "Subject added successfully!")
            return redirect("/administrator/subject")
        else:
            messages.error(request, "Error in registration for Subject!")
    else:  
        form = SubjectForm()  
    return redirect("/administrator/subject",{'form':form})


# Student Upload
def student(request):
    Students = Student.objects.all().order_by('-id')
    p = Paginator(Students, 10)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except Paginator.PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except Paginator.EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = { 'page_obj': page_obj } 
    return render(request,'student.html', context) 

def upload_csv(request):
    data = {}
    if "GET" == request.method:
        return render(request, "student.html", data)
    
    # if not GET, then proceed
    csv_file = request.FILES["csv_file"]
    
    # return HttpResponse(csv_file.name)
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'File is not CSV type')
        return redirect("/administrator/student")
    
    #if file is too large, return
    if csv_file.multiple_chunks():
        messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
        return redirect("/administrator/student")


    file_data = csv_file.read().decode("utf-8")		

    lines = file_data.split("\n")
    
    try:        
        for line in lines:
            fields = line.split(",")
            form = Student(
                enrolment = fields[0],
                seatno = fields[1],     
                name = fields[2],
                email = fields[3],
                phoneno = fields[4],
                gender = fields[5],
                category = fields[6]
            )
            form.save()
    except:
        messages.success(request, "Student data uploaded successfully!")
        
    unique_fields = ['enrolment']
    duplicates = (
        Student.objects.values(*unique_fields)
        .order_by()
        .annotate(max_id=Max('id'), count_id=Count('id'))
        .filter(count_id__gt=1)
    )
    
    for duplicate in duplicates:
        (
            Student.objects
            .filter(**{x: duplicate[x] for x in unique_fields})
            .exclude(id=duplicate['max_id'])
            .delete()
        )        
    return redirect("/administrator/student")
