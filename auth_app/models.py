from django.db import models

import datetime
import os


# Create your models here.
def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class users(models.Model):
    username = models.TextField(max_length = 50)
    email = models.EmailField(blank = True,max_length=50)
    phoneno = models.TextField(max_length = 10)
    password = models.TextField(max_length = 50)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)
    type = models.IntegerField()
    def __str__(self):
        return self.name  