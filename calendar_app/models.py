from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    start_date = models.DateField()
    end_date = models.DateField()

    start_time = models.TimeField()
    end_time = models.TimeField()

    all_day_event = models.BooleanField()

    id=models.AutoField(primary_key=True)

    def __str__(self):
        return self.title
