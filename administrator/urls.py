from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.adminIndex, name="adminIndex"), # admin index page
    path('faculty',views.faculty,name="faculty"),
    path('addFaculty', views.addFaculty, name="addFaculty"),
    path('deleteFaculty<id>', views.deleteFaculty, name="deleteFaculty"), 

    #Batch urls ::

    path('batch',views.batch,name='batch'),
    path('addBatch', views.addBatch, name="addBatch"),


]