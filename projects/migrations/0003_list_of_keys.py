# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-02 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20170928_0258'),
    ]

    operations = [
        migrations.CreateModel(
            name='list_of_keys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50)),
            ],
        ),
    ]