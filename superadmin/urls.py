from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.indexDashboard, name="indexDashboard"),
    path('profile', views.profile, name="profile"),
    path('institute', views.institute, name="institute"),
    # path('addInstitute', views.addInstitute, name="addInstitute"),
]