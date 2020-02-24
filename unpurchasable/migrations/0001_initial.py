# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-23 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='filter_piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piece_filter', models.CharField(choices=[('25', 'Logo'), ('20', 'Clothing'), ('30', 'WebApp'), ('35', 'Advertising'), ('40', 'Illistration'), ('15', 'Packaging')], default='', max_length=50)),
            ],
        ),
    ]