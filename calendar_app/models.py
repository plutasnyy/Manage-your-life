from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    start_date = models.DateField(error_messages={'required': 'Please enter your start date'})
    end_date = models.DateField(error_messages={'required': 'Please enter your end date'})

    start_time = models.TimeField(error_messages={'required': 'Please enter your start time'})
    end_time = models.TimeField(error_messages={'required': 'Please enter your end time'})

    all_day_event = models.BooleanField()

    id=models.AutoField(primary_key=True)

    def __str__(self):
        return self.title
