from django.db import models

# Create your models here.
class Institute(models.Model):
    instituteID = models.IntegerField(unique=True)
    instituteName = models.TextField(blank = True, max_length=50)
    instituteAddress = models.TextField(max_length=150)
