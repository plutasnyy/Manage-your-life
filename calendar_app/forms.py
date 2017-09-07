from django import forms
from calendar_app.models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        exclude=('modified', )
        fields=['title','start_date','end_date', ]
