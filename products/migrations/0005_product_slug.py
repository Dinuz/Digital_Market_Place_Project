# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20160714_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='slug-field'),
        ),
    ]