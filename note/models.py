from django.db import models
from datetime import datetime

class Note(models.Model):
    title=models.CharField(max_length=64)
    created_on=models.DateTimeField(auto_now_add=True)
    content=models.CharField(max_length=5000)

    def __str__(self):
        return self.name
