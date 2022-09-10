from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.indexDashboard, name="indexDashboard"),
    path('profile', views.profile, name="profile"),
    path('institute', views.institute, name="institute"),
    path('course', views.course, name="course"),
    # Institute CRUD paths
    path('addInstitute', views.addInstitute, name="addInstitute"),
    path('showInstitute', views.showInstitute, name="showInstitute"),
    path('deleteInstitute<id>', views.deleteInstitute, name="deleteInstitute"),
    # Course CRUD paths
    path('addCourse', views.addCourse, name="addCourse"),
    
]