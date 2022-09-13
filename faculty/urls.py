from django.urls import path
from . import views

urlpatterns = [
    path('', views.facultyIndex, name="facultyIndex"),
]