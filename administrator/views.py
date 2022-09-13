from django.shortcuts import render

# Create your views here.
def adminIndex(request):
    return render(request, 'index.html')

# Admin CRUD starts 
def admin(request):
    context ={"Admin":users.objects.all().filter(type="2")}
    return render(request,'admin.html',context)

def addFaculty(request):
    if request.method == "POST":     
        form = RegisterForm(request.POST or None)  
        if form.is_valid():  
            form.save()  
            messages.success(request, "You are registered sucessfully in as {username}!")
            return redirect("/administrator/faculty")
            #return render(request,'admin.html')  
        else:
            messages.error(request, "Registration failed! {username}!")
    else:  
        form = RegisterForm()  
    return redirect("/administrator/faculty",{'form':form})

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
            messages.success(request, "Admin updation successfully!")
        else:
            messages.error(request, "Admin updation failed!")
        return redirect("/superadmin/admin")

    context['form'] = form
    return redirect("/superadmin/admin", context)

def deleteAdmin(request,id):
    context ={}
    obj = get_object_or_404(users,id=id)
    if request.method == "GET":
        if obj.delete():
            messages.success(request,"Data deleted successfully for Id : " + str(id))
            return redirect("/superadmin/admin")
        else:
            messages.error(request," deletion failed for Id : " + str(id))
    return render(request,'admin.html',context)
# Admin CRUD ends here

