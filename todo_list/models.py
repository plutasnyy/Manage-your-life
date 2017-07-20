from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Item(models.Model):
    id=models.AutoField(primary_key=True)
    list=models.ForeignKey(List)
    content=models.TextField())
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class List(models.Model):
    id=models.AutoField(primary_key=True)
    created_by=ForeignKey(User)
    title=models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
