from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.adminIndex, name="adminIndex"), # admin index page
    path('addFaculty', views.addFaculty, name="addFaculty"), # admin index page

]