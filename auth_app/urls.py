from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('facultyRegister', views.faculty_register, name="register"),
]