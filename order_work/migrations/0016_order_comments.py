# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-26 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_work', '0015_auto_20200226_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comments',
            field=models.CharField(default='', max_length=200),
        ),
    ]