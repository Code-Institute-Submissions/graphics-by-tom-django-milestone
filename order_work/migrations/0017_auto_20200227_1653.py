# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-27 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_work', '0016_order_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]