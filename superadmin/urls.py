from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [    
    path('', views.indexDashboard, name="indexDashboard"),
    path('profile', views.profile, name="profile"),
    
    # institute urls
    path('institute', views.institute, name="institute"),
    path('addInstitute', views.addInstitute, name="addInstitute"),
    path('updateInstitute<instituteID>', views.updateInstitute, name="updateInstitute"),
    path('editInstitute/<instituteID>', views.editInstitute, name="editInstitute"),
    path('deleteInstitute<instituteID>', views.deleteInstitute, name="deleteInstitute"),

    # course urls
    path('course', views.course, name="course"),
    path('addCourse', views.addCourse, name="addCourse"),
    path('updateCourse<courseID>', views.updateCourse, name="updateCourse"),
    path('editCourse/<courseID>', views.editCourse, name="editCourse"),
    path('deleteCourse/<courseID>', views.deleteCourse, name="deleteCourse"),

    #admin urls
    path('admin', views.admin,name="admin"),
    path('addAdmin', views.addAdmin, name="addAdmin"),
    path('updateAdmin<id>', views.updateAdmin, name="updateAdmin"),
    path('editAdmin/<id>', views.editAdmin, name="editAdmin"),
    path('deleteAdmin<id>', views.deleteAdmin, name="deleteAdmin"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)