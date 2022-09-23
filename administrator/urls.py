from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.adminIndex, name="adminIndex"), # admin index page
    path('faculty',views.faculty,name="faculty"),
    path('addFaculty', views.addFaculty, name="addFaculty"),
    path('editFaculty/<id>', views.editFaculty, name="editFaculty"),
    path('updateFaculty<id>', views.updateFaculty, name="updateFaculty"), 
    path('deleteFaculty<id>', views.deleteFaculty, name="deleteFaculty"), 
]