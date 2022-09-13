from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from auth_app.models import users
from auth_app.forms import RegisterForm

# Create your views here.
def adminIndex(request):
    return render(request, 'index_admin.html')

# Admin CRUD starts 
def faculty(request):
    context ={"faculty":users.objects.all().filter(type="3")}
    return render(request,'faculty.html',context)

def addFaculty(request):
    if request.method == "POST":     
        form = RegisterForm(request.POST or None)  
        if form.is_valid():  
            form.save()  
            messages.success(request, "Faculty added successfully!")
            return redirect("/administrator/faculty")
            #return render(request,'admin.html')  
        else:
            messages.error(request, "Error in registration for faculty!")
    else:  
        form = RegisterForm()  
    return redirect("/administrator/faculty",{'form':form})

# Request Update Admin Page
def updateAdmin(request,id):
    context = users.objects.get(id=id)
    return render(request, "updateAdmin.html",{'context' : context})

# Update Function Of Admin
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

