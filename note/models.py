from django.db import models
from datetime import datetime

from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    author = models.ForeignKey('auth.User')

    def __str__(self):
        return self.name
