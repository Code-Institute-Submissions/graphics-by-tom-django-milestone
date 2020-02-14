# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-14 12:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order_work', '0004_order_order_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name_or_company', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=20)),
                ('current_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='purchase_line_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.purchase')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_work.order')),
            ],
        ),
    ]
