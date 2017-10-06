from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200, help_text = "Event Name: ")
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    start_date = models.DateField(error_messages = {'required': 'Please enter your start date'},
                                help_text = 'Start Date: ')
    end_date = models.DateField(error_messages = {'required': 'Please enter your end date'},
                                help_text = "End Date: ")


    all_day_event = models.BooleanField(help_text = "All Day:")

    start_time = models.TimeField(help_text = "Start Time: ")
    end_time = models.TimeField(help_text = "End Time: ")


    id=models.AutoField(primary_key=True)

    def __str__(self):
        return self.title
