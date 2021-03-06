# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-03-31 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('avatar', models.ImageField(upload_to='user')),
            ],
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': '员工', 'verbose_name_plural': '员工'},
        ),
    ]
