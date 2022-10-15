from django.urls import path
from . import views

urlpatterns = [
    path('', views.facultyIndex, name="facultyIndex"), #marks_entry_page
    path('marks_entry_page', views.marks_entry_page, name="marks_entry_page"),
    path('marks_entry/<course_id>/<course_name>/', views.marks_entry, name="marks_entry"),
]