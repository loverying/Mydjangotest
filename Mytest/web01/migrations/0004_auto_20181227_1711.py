# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-27 09:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web01', '0003_auto_20181225_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='commandiog',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='保存日期'),
        ),
        migrations.AlterField(
            model_name='commandiog',
            name='command',
            field=models.CharField(max_length=128),
        ),
    ]