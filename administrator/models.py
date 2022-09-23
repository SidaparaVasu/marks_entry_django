from django.db import models
from superadmin.models import Course
# Create your models here.
class Batch(models.Model):
    batchID = models.AutoField(primary_key=True)
    batchName = models.TextField(blank = True, max_length=50)
    courseName = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='course')