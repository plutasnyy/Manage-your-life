from django.shortcuts import render

def Homepage(request):
    return render(request,'note.html',{})
