# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20160714_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=6.99, max_digits=100, null=True),
        ),
    ]
