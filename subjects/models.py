from django.db import models
from datetime import datetime


class SubjectModel(models.Model):
    subject_name = models.CharField(default='', max_length=200)
    email = models.EmailField(default='')
    title = models.CharField(default='empty', max_length=100)
