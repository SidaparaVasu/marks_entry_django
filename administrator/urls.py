from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('', views.adminIndex, name="adminIndex"), # admin index page
    
    # faculty
    path('faculty',views.faculty,name="faculty"),
    path('addFaculty', views.addFaculty, name="addFaculty"),
    path('editFaculty/<id>', views.editFaculty, name="editFaculty"),
    path('updateFaculty<id>', views.updateFaculty, name="updateFaculty"), 
    path('deleteFaculty<id>', views.deleteFaculty, name="deleteFaculty"), 
    
    # batch
    path('batch',views.batch,name="batch"),
    path('addBatch', views.addBatch, name="addBatch"),
    

    # Semester
    path('semester',views.semester,name="semester"),
    path('addSemester', views.addSemester, name="addSemester"),
    path('updateSemester<id>', views.updateSemester, name="updateSemester"), 

    # Subject
    path('subject',views.subject,name="subject"),
    path('addSubject', views.addSubject, name="addSubject"),
<<<<<<< HEAD
    path('fetch_semesters/<course_id>/<course_name>/', views.fetch_semesters, name="fetch_semesters"),
=======
    # path('fetch_semesters/<course_id>/<course_name>/', views.fetch_semesters, name="fetch_semesters"),
    # path('fetch_semesters', views.fetch_semesters, name="fetch_semesters"),addSubject
    
>>>>>>> vasu_v
    
    # Student
    path('student', views.student, name="student"),
    path('upload_csv', views.upload_csv, name='upload_csv'),
]