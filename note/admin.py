from django.contrib import admin
from note.models import Note
from todo_list.models import List, Item
admin.site.register(List)
admin.site.register(Item)
admin.site.register(Note)
# Register your models here.
