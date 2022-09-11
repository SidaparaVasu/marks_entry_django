from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.indexDashboard, name="indexDashboard"),
    path('profile', views.profile, name="profile"),
    
    # institute urls
    path('institute', views.institute, name="institute"),
    path('addInstitute', views.addInstitute, name="addInstitute"),
    path('updateInstitute<id>', views.updateInstitute, name="updateInstitute"),
    path('editInstitute/<id>', views.editInstitute, name="editInstitute"),
    path('deleteInstitute<id>', views.deleteInstitute, name="deleteInstitute"),

    # course urls
    path('course', views.course, name="course"),
    path('addCourse', views.addCourse, name="addCourse"),
    path('updateCourse<id>', views.updateCourse, name="updateCourse"),
    path('editCourse/<id>', views.editCourse, name="editCourse"),
    path('deleteCourse<id>', views.deleteCourse, name="deleteCourse"),
    
]