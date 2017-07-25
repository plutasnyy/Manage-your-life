from django import forms
from todo_list.models import List,Item

class ListForm(forms.ModelForm):
    class Meta:
        model=List
        exclude=('modified',)
        fields=['title']

class ItemForm(forms.Form):
    Field=forms.CharField()
