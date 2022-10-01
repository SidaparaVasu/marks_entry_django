from django.db import models

# Create your models here.
class Institute(models.Model):
    instituteID = models.AutoField(primary_key=True)
    instituteName = models.TextField(blank = True, max_length=50)
    instituteAddress = models.TextField(max_length=150)

class Course(models.Model):
    courseID =  models.AutoField(primary_key=True)
    courseName = models.TextField(blank = True, max_length=50)
    num_of_semesters = models.TextField(blank = False, max_length=2)
    instituteName = models.ForeignKey(Institute, on_delete=models.CASCADE,related_name='institute')