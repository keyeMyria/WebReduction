# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-19 19:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experiment',
            old_name='experiment_number',
            new_name='number',
        ),
    ]