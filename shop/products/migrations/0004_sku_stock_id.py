# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20170613_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='sku',
            name='stock_id',
            field=models.CharField(default=0, max_length=50, unique=True),
            preserve_default=False,
        ),
    ]