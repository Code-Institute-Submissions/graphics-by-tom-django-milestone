# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-28 12:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_work', '0017_auto_20200227_1653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='paid',
            new_name='paid_tf',
        ),
    ]