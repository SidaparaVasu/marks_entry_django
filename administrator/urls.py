from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.adminIndex, name="adminIndex"), # admin index page
]