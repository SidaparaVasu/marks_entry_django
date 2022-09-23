from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name="loginPage"),
    path('register', views.registerPage, name="registerPage"),
    path('registration', views.registration, name="registration"),
    path('loginHandle', views.loginHandle, name="loginHandle"),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)