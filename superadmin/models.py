from django.db import models

# Create your models here.
class addInstitute(models.Model):
    instituteId = models.TextField(max_length = 10,default)
    instituteName = models.TextField(blank = True, max_length = 50)
    instituteAddress = models.TextField(max_length = 50)