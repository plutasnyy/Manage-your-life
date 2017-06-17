from django.shortcuts import render
from django.views.generic.edit import CreateView

def Homepage(request):
    return render(request,'index.html',{})
