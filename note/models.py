from django.db import models
from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=200,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True)
    created_by = models.ForeignKey(User, related_name='todo_created_by',null=True)
    id=models.AutoField(primary_key=True)

    def __str__(self):
        return self.title
