# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-30 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
