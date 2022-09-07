from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect 
from . models import Institute

# Create your views here.
def indexDashboard(request):
    return render(request, "index.html")

def profile(request):
    return render(request, "profile.html")

def institute(request):
    return render(request, "institute.html")