# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-25 08:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web01', '0002_auto_20181225_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commandiog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
