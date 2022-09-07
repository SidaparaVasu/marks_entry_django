from django.db import models

# Create your models here.
class Institute(models.Model):
    instituteId = models.TextField(max_length = 10, primary_key=True)
    instituteName = models.TextField(blank = True, max_length = 50)
    instituteAddress = models.TextField(max_length = 75)