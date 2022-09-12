from django.db import models

# Create your models here.
class Institute(models.Model):
    instituteID = models.IntegerField(unique=True)
    instituteName = models.TextField(blank = True, max_length=50)
    instituteAddress = models.TextField(max_length=150)

class Course(models.Model):
    courseID = models.IntegerField(unique=True)
    courseName = models.TextField(blank = True, max_length=50)
    instituteName = models.ForeignKey(Institute, on_delete=models.CASCADE,related_name='institute')