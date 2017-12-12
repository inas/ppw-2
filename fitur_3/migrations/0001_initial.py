# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-12 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                # ('pengguna_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                # ('pengguna_id', models.CharField(max_length=100, primary_key=True, unique=True)),
                ('pengguna', models.CharField(max_length=100, null=True, default='not-set')),
                ('message', models.TextField(null=True, default='not-set')),
                ('title' , models.CharField(max_length=140, null=True, default='not-set')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
