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
from django.conf.urls import url,include
from django.contrib import admin


from django.views.generic.base import TemplateView

import main.views
import note.views
import calendar_app.views

#main
urlpatterns = [
    url(r'^registration/$',main.views.signup,name='Registration'),
    url(r'^logout/$', main.views.logout_view, name='Logout'),
    url(r'^$', main.views.Homepage.as_view(),name="Homepage"),
    url(r'^admin/', admin.site.urls),
]

#note
urlpatterns+=[

    url(r'^note/edit/(?P<pk>[0-9]+)$',note.views.NoteUpdate.as_view(),name='Note Update'),
    url(r'^note/delete/(?P<id>[0-9]+)$',note.views.note_delete,name='Note Delete'),
    url(r'^note$',note.views.homepage,name='Note Homepage'),
]

#todo_list
urlpatterns+=[
    url(r'^todo_list/', include('todo_list.urls',namespace='todo_list')),
]

#calendar_app
urlpatterns+=[
    url(r'^calendar$',calendar_app.views.Homepage,name='Calendar Homepage'),
]
