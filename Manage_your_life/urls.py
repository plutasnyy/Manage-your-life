"""Manage_your_life URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.contrib.auth import views as auth_views
    
import main.views
import note.views
import calendar_app.views
import todo_list.views

#main
urlpatterns = [

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^$', main.views.Homepage,name="Homepage"),
    url(r'^admin/', admin.site.urls),
]

#note
urlpatterns+=[
    url(r'^note$',note.views.Homepage,name='Note Homepage'),
]

#todo_list
urlpatterns+=[
    url(r'^todo_list$',todo_list.views.Homepage,name='Todo_list Homepage'),
]

#calendar_app
urlpatterns+=[
    url(r'^calendar$',calendar_app.views.Homepage,name='Calendar Homepage'),
]
