# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Use pen name, not real name!', max_length=70, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('review', models.TextField(blank=True, null=True)),
                ('date_reviewed', models.DateTimeField(blank=True, null=True)),
                ('is_favourite', models.BooleanField(default=False, verbose_name='Favourite?')),
                ('authors', models.ManyToManyField(related_name='books', to='books.Author')),
            ],
        ),
    ]
