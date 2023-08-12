from datetime import datetime
from django.db import models
class ToDoModel(models.Model):
    Task_name = models.CharField(default='', max_length=100)
    Created_at = models.DateTimeField(datetime.now)
    Done = models.BooleanField(default="False")
    Updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Task_name