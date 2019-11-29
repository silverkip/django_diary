from django.db import models
from datetime import datetime

class Diary(models.Model):
  title = models.CharField(max_length=256)
  content = models.TextField(default="")
  date = models.DateField(default=datetime.now())
  created = models.DateTimeField(default=datetime.now())
  edited = models.DateTimeField(null=True,  blank=True)