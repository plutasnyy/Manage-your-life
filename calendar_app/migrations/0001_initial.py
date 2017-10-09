# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-09 08:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('title', models.CharField(help_text='Event Name: ', max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateField(error_messages={'required': 'Please enter your start date'}, help_text='Start Date: ')),
                ('end_date', models.DateField(error_messages={'required': 'Please enter your end date'}, help_text='End Date: ')),
                ('all_day_event', models.BooleanField(help_text='All Day:')),
                ('start_time', models.TimeField(help_text='Start Time: ')),
                ('end_time', models.TimeField(help_text='End Time: ')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
