from django.shortcuts import render

# Create your views here.
def indexDashboard(request):
    return render(request, "index.html")

def profile(request):
    return render(request, "profile.html")

def addInstitute(request):
    return render(request, "addInstitute.html")