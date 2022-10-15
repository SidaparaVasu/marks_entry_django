from django.shortcuts import render, redirect, get_object_or_404,HttpResponse 
from django.contrib import messages
from django.http import HttpResponseRedirect
from administrator.models import Semester
from administrator.views import semester
from superadmin.models import Course

# Create your views here.
def facultyIndex(request):
    return render(request, 'index_faculty.html')

def marks_entry_page(request):
    courses = Course.objects.all()
    return render(request, 'marks_entry.html', {'courses':courses})

def marks_entry(request, course_id, course_name):
    courses = Course.objects.all()
    semesters = Semester.objects.all().filter(courseName_id=course_id)
    myDict = {
        'courses':courses,
        'semesters':semesters,
        'selected_course':course_name,
    }
    return render(request, 'marks_entry.html', myDict)
    # return redirect("/faculty/marks_entry", {'myDict':myDict})
