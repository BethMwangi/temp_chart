# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-02 20:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('temp_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempchart',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='tempchart',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
