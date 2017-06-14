# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 05:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileApp', '0008_auto_20170612_1052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='mobile',
        ),
        migrations.AddField(
            model_name='profile',
            name='mobile_no',
            field=models.BigIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(9999999999L)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=b'profile'),
        ),
    ]