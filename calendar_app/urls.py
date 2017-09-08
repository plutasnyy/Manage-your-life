from django.conf.urls import url

import calendar_app.views as calendar

urlpatterns=[
    url(r'^$',calendar.homepage,name='Homepage'),
    url(r'^create/$',calendar.create_event,name='CreateEvent'),
    ]
