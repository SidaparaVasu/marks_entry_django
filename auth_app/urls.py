from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name="loginPage"),
    path('register', views.registerPage, name="registerPage"),
    path('registration', views.registration, name="registration"),
    path('loginHandle', views.loginHandle, name="loginHandle"),
    path('logoutHandle', views.logoutHandle, name="logoutHandle"),
]