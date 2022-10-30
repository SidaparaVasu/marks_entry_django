from django.views.decorators.cache import cache_control
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from auth_app.forms import RegisterForm  
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
# from django.contrib.sessions import sessions
from . models import users
from django.forms.models import model_to_dict

# logger
import logging,traceback
logger = logging.getLogger('authLogger')
#


# Create your views here.
def loginPage(request):
    return render(request, 'login.html')

def registerPage(request):
    return render(request, 'register.html')

def registration(request):
    if request.method == "POST":     
        form = RegisterForm(request.POST or None)  
        if form.is_valid():  
            form.save()  
            messages.success(request, "You are registered sucessfully in as {username}!")
            return render(request,'login.html')  
        else:
            messages.error(request, "Registration failed! {username}!")
    else:  
        form = RegisterForm()  
    return render(request,'register.html',{'form':form})  

def loginHandle(request):
    if request.method == "POST":    
        form = RegisterForm(request.POST)
        un = request.POST.get("username")
        ps = request.POST.get("password")
        image_path = request.POST.get("image")

        row_counter = users.objects.all().count()
        if row_counter == 0:
            form = users(username='superadmin', email='superadmin@gmail.com', phoneno=9852360147,
                                password=12345, image='', type=1)
            form.save()
            messages.success(request, "please login again!")
            return render(request,'login.html')  
        else:
            flag = 0
            try:
                data = users.objects.all()
                # return HttpResponse(data)
                
                for i in range(len(data)):
                    if data[i].username == un and data[i].password == ps:
                        request.session['username'] = data[i].username
                        request.session['email'] = data[i].email
                        request.session['phoneno'] = data[i].phoneno
                    
                        username = request.session['username']
                        email = request.session['email']
                        phoneno = request.session['phoneno']
                        session_user = {'username': username, 'email': email, 'phoneno': phoneno, 'image_path': image_path}
                        
                        if data[i].type == 1:
                            logger.info("super admin: " + data[i].username + " is logged in")
                            return HttpResponseRedirect('/superadmin', session_user)
                        elif data[i].type == 2:
                            logger.info("admin: " + data[i].username + " is logged in")
                            return HttpResponseRedirect('/administrator', session_user)
                        elif data[i].type == 3:
                            logger.info("faculty: " + data[i].username + " is logged in")
                            return HttpResponseRedirect('/faculty', session_user)
                    else:
                        flag = 1
                if flag == 1:
                    html = "Invaild Credentials! Please try again!" + "<a href='login'>Go back</a>"
                    return HttpResponse(html)
            except:
                messages.error(request, "please check your credentials and try again!")
                return render(request,'login.html')  
    else:
        form = RegisterForm()
        return render(request, template_name = "login.html")


SESSION_EXPIRE_AT_BROWSER_CLOSE = True
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logoutHandle(request):
    try:
        del request.session['username']
        del request.session['email']
        del request.session['phoneno']
    except KeyError:
        pass
    messages.success(request, "You are Logged out!")
    return HttpResponseRedirect('/auth/loginHandle')