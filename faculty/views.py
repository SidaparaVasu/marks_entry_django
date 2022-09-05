from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from faculty import templates 
def index(request):
    return render(request,'index.html')