# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-09 02:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 9, 2, 25, 39, 913835, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
