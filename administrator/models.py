from django.db import models
from superadmin.models import Course
# Create your models here.
class Batch(models.Model):
    batchID = models.AutoField(primary_key=True)
    batchName = models.TextField(blank = True, max_length=50)
    courseName = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='course1')

class Semester(models.Model):
    semesterId = models.AutoField(primary_key=True)
    semester = models.IntegerField()
    courseName = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='course')

class Subject(models.Model):
    subjectId = models.AutoField(primary_key=True)
    subject = models.TextField(blank = True, max_length=40)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE,related_name='semester1')
    credits = models.IntegerField()