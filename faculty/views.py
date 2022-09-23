from django.shortcuts import render, redirect, get_object_or_404,HttpResponse 
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def facultyIndex(request):
    return render(request, 'index_faculty.html')