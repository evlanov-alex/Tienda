# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 14:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0004_auto_20170620_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='phone',
        ),
    ]
