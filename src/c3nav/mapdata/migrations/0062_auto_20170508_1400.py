# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-08 14:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapdata', '0061_auto_20170507_0953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['altitude'], 'verbose_name': 'Section', 'verbose_name_plural': 'Sections'},
        ),
    ]
