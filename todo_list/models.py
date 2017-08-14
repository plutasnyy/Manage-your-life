from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class List(models.Model):
    id=models.AutoField(primary_key=True)
    created_by=models.ForeignKey(User)
    title=models.TextField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Item(models.Model):
    id=models.AutoField(primary_key=True)
    list=models.ForeignKey(List)
    content=models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    executed=models.BooleanField(default=False)

    def __str__(self):
        return self.content
