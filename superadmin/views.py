from django.shortcuts import render

# Create your views here.
def indexDashboard(request):
    return render(request, "index.html")