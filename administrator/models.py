from enum import unique
from unittest.util import _MAX_LENGTH
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
    courseName = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='course2')

class Subject(models.Model):
    subjectId = models.AutoField(primary_key=True)
    courseName = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='course3')
    subject = models.TextField(blank = True, max_length=40)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE,related_name='semester1')
    credits = models.IntegerField()
    
class Student(models.Model):
    enrolment = models.BigIntegerField(blank = True )
    seatno = models.TextField(max_length=20, blank = True)
    name = models.TextField(max_length=50, blank = True)
    email = models.EmailField(max_length=50, blank = True)
    phoneno = models.TextField(max_length = 10, blank = True)
    gender = models.TextField(max_length = 6, blank = True)
    category = models.TextField(max_length = 10, blank = True)
    