from django.db import models

# Create your models here.
class admin(models.Model):
    adminname = models.TextField(max_length=20)
    adminpassword = models.TextField(max_length=8)

class users(models.Model):
    username = models.TextField(max_length = 50)
    email = models.EmailField(blank = True,max_length=50)
    phoneno = models.TextField(max_length = 10)
    password = models.TextField(max_length = 50)
    def __str__(self):
        return self.name 