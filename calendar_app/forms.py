from django import forms
from calendar_app.models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        exclude=('modified', )
        fields=['title', s]
