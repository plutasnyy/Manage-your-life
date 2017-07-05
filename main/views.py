from django.shortcuts import render

def Homepage(request):
    template_name='index.html'
    return render(request,'index.html',{})
