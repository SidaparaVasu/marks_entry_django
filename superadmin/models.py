from django.db import models

# Create your models here.
class Institute(models.Model):
    instituteId = models.TextField(unique=True, max_length=11)
    instituteName = models.TextField(blank = True, max_length=50)
    instituteAddress = models.TextField(max_length=75)
