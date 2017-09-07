from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    date = models.ForeignKey(DateTimeField)
    id=models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.title
