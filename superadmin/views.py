from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse 
from superadmin.models import Institute, Course
from superadmin.forms import InstituteForm, CourseForm
from auth_app.models import users
from auth_app.forms import RegisterForm
from django.conf import settings
from django.core.mail import send_mail

from django.core.paginator import Paginator

from administrator.models import Semester


# logger
import logging,traceback
logger = logging.getLogger('superadminLogger')
#


# Create your views here.
def indexDashboard(request):
    return render(request, "index.html")

def profile(request):
    return render(request, "profile.html")

# Institute CRUD starts here
def institute(request):
    Institutes = Institute.objects.all().order_by('-instituteID')
    p = Paginator(Institutes, 10)
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
    return render(request,'institute.html',context)  

def addInstitute(request):
    if request.method == "POST":     
        form = InstituteForm(request.POST or None) 
        if form.is_valid():   
            if form.save():
                logger.info("Institute added!")
                messages.success(request, "Institute added successfully!")
                return redirect("/superadmin/institute") 
            else:
                logger.info("Institute insertion failed!")
                messages.error(request, "Institute insertion failed!")
        else:
            messages.error(request, "Form is not valid! please fill up form curreclty!")
        return redirect("/superadmin/institute")
    else:  
        form = InstituteForm()  
    return redirect("/superadmin/institute",{'form':form})

# Request UpdateInstitute Page
def updateInstitute(request,instituteID):
    context = Institute.objects.get(instituteID=instituteID)
    return render(request, "updateInstitute.html",{'context' : context})

# Update Function Of Institute
def editInstitute(request,instituteID):
    context = {}
    obj = get_object_or_404(Institute, instituteID=instituteID)
    form = InstituteForm(request.POST or None, instance=obj)

    if form.is_valid():
        if form.save():
            logger.info("Institute updation successfully!")
            messages.success(request, "Institute updation successfully!")
            return redirect("/superadmin/institute")
        else:
            logger.info("Institute updation failed!")
            messages.error(request, "Institute updation failed!")
    else:
        messages.error(request, "Form is not valid! please fill up form curreclty!")
    context['form'] = form
    return redirect("/superadmin/institute",context)

def deleteInstitute(request,instituteID):
    context ={}
    obj = get_object_or_404(Institute,instituteID=instituteID)
    if request.method == "GET":
        if obj.delete():
            logger.info("Institute deleted successfully for Id : " + str(instituteID))
            messages.success(request,"Institute deleted successfully for Id : " + str(instituteID))
            return redirect("/superadmin/institute")
        else:
            logger.info("Institute deleted successfully for Id : " + str(instituteID))
            messages.error(request,"Institute deletion failed for Id : " + str(instituteID))
    return render(request,'institute.html',context)
# Institute CRUD ends here


# Course CRUD starts here
def course(request):
    Courses = Course.objects.all().select_related('instituteName').order_by('-courseID')
    p = Paginator(Courses, 10)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except Paginator.PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except Paginator.EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj, 'Institutes':Institute.objects.all().order_by('-instituteID')} 
    return render(request,'course.html',context)
    # context ={"Course":Course.objects.all().select_related('instituteName').order_by('-courseID'),'Institutes':Institute.objects.all().order_by('-instituteID')}

def addCourse(request):
    if request.method == "POST":     
        c_form = CourseForm(request.POST or None) 
        courseName = request.POST.get('courseName')

        if c_form.is_valid(): 
            if c_form.save():
                logger.info(f"Course { courseName } added successfully")
                
                num_of_semesters = request.POST.get('num_of_semesters')
    
                for sem in range(1,int(num_of_semesters)+1):
                    course_data = Course.objects.all()
                    tot_course_data = Course.objects.all().count()
                    # return HttpResponse((course_data[tot_course_data-1].courseID))
                    s_form = Semester(semester=sem, courseName_id=(course_data[tot_course_data-1].courseID))
                    # return HttpResponse(course_data[tot_course_data-1].courseID)
                    s_form.save()
                
                    logger.info(f"Semester { sem } added successfully for Course { courseName }")
                messages.success(request, "Course added successfully!")
                return redirect("/superadmin/course")
            else:
                messages.success(request, "Course insertion failed!")
    else:  
        c_form = CourseForm()  
    return redirect("/superadmin/course",{'c_form':c_form})

# Request UpdateCourse Page
def updateCourse(request,courseID):
    context = Course.objects.get(courseID=courseID)
    return render(request, "updateCourse.html",{'context' : context})

# Update Function Of Course
def editCourse(request,courseID):
    context = {}
    obj = get_object_or_404(Course, courseID=courseID)
    form = CourseForm(request.POST or None, instance=obj)

    if form.is_valid():
        if form.save():
            logger.info("Course updation successfully!")
            messages.success(request, "Course updation successfully!")
            return redirect("/superadmin/course")
        else:
            logger.info("Course updation failed!")
            messages.error(request, "Course updation failed!")
    else:
        messages.error(request, "Form is not valid! please fill up form curreclty!")
    context['form'] = form
    return redirect("/superadmin/course",context)


def deleteCourse(request,courseID):
    context ={}
    obj = get_object_or_404(Course,courseID=courseID)
    if request.method == "GET":
        if obj.delete():
            logger.info("Course deleted successfully for Id : " + str(courseID))
            messages.success(request,"Course deleted successfully for Id : " + str(courseID))
            return redirect("/superadmin/course")
        else:
            logger.info("Course deleted failed for Id : " + str(courseID))
            messages.error(request,"Course deletion failed for Id : " + str(courseID))
    return render(request,'course.html',context)
# Course CRUD ends here


# Admin CRUD starts 
def admin(request):
    admins = users.objects.all().filter(type="2").order_by('-id')
    
    p = Paginator(admins, 10)
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
    return render(request,'admin.html',context) 

def addAdmin(request):
    if request.method == "POST":     
        form = RegisterForm(request.POST or None, request.FILES) 
        un = request.POST.get("username")
        ps = request.POST.get("password") 
        email = request.POST.get("email") 
        if len(request.FILES) != 0:
            form.image = request.FILES['image']
        if form.is_valid():  
            if form.save():                 
                # sending email to added admin 
                subject = f'welcome {un}!!!'
                message = f'Greetings! You are registered as an admin. Your Username: { un }, Your Password: { ps }'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]

                send_mail( subject, message, email_from, recipient_list )
                
                logger.info("Admin added successfully!")
                messages.success(request, "Admin added successfully!")
                return redirect("/superadmin/admin") 
            else:
                logger.info("Admin added failed!")
                messages.error(request, "Admin insertion failed!")  
        else:
            messages.error(request, "Form is not valid! please fill up form curreclty!")
    else:  
        form = RegisterForm()  
    return redirect("/superadmin/admin",{'form':form})

# Request Update Admin Page
def updateAdmin(request,id):
    context = users.objects.get(id=id)
    return render(request, "updateAdmin.html",{'context' : context})

# Update Function Of Admin
def editAdmin(request,id):
    context = {}
    obj = get_object_or_404(users, id=id)
    form = RegisterForm(request.POST or None, instance=obj)

    if form.is_valid():
        if form.save():
            logger.info("Admin updation successfully!")
            messages.success(request, "Admin updation successfully!")
            return redirect("/superadmin/admin")
        else:
            logger.info("Admin updation failed!")
            messages.error(request, "Admin updation failed!")
    else:
        messages.error(request, "Form is not valid! please fill up form curreclty!")
    context['form'] = form
    return redirect("/superadmin/admin", context)

def deleteAdmin(request,id):
    context ={}
    obj = get_object_or_404(users,id=id)
    if request.method == "GET":
        if obj.delete():
            logger.info(request,"Admin deleted successfully for Id : " + str(id))
            messages.success(request,"Admin deleted successfully for Id : " + str(id))
            return redirect("/superadmin/admin")
        else:
            logger.info(request,"Admin deleted failed for Id : " + str(id))
            messages.error(request,"Admin deletion failed for Id : " + str(id))
    return render(request,'admin.html',context)
# Admin CRUD ends here