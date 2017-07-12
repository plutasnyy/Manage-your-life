from django import forms
from note.models import Note

class NoteForm(forms.ModelForm):
    model=Note
    exclude=('modified', )
