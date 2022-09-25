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

    #Subject
    path('subject',views.subject,name="subject"),
    path('addSubject', views.addSubject, name="addSubject"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)