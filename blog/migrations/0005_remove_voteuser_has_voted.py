# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-13 16:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170113_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voteuser',
            name='has_voted',
        ),
    ]
