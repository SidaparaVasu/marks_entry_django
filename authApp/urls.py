from django.contrib import admin
from django.urls import path

from authApp.views import loadAuth
# from authApp import views

urlpatterns = [
    path('', loadAuth),
]