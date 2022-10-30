from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse 
from django.contrib import messages
from django.http import HttpResponseRedirect
from administrator.models import Batch,Semester,Subject,Student
from administrator.views import semester
from superadmin.models import Course,Institute

# Create your views here.
def facultyIndex(request):
    return render(request, 'index_faculty.html')

def marks_entry(request):
    context = {
        'institutes' : Institute.objects.all().order_by('-instituteID')
    }
    return render(request, 'marks_entry.html', context)

def load_students(request):
    institute_id = request.GET.get('institute_id')
    course_id = request.GET.get('course_id')
    batch_id = request.GET.get('batch_id')
    semester_id = request.GET.get('semester_id')
    
    students = Student.objects.all().filter(instituteName_id=institute_id) \
                .filter(courseName_id=course_id).filter(batchName_id=batch_id) \
                .filter(semester_id=semester_id).order_by('enrolment'),
    subjects = Subject.objects.all().filter(courseName_id=course_id).filter(semester_id=semester_id).order_by('subject'),

    return render(request, 'marks_entry_form.html', {
        'students': students, 'subjects':subjects
    })