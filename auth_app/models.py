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
    type = models.IntegerField(max_length = 1, default = 3)
    # def __str__(self):
    #     return (self.username,self.email)
    def data(self):
        return [self.username,self.email]