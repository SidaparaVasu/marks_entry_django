from django.db import models

# Create your models here.
class admin(models.Model):
    adminname = models.TextField(max_length=20)
    adminpassword = models.TextField(max_length=8)