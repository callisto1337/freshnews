# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_remove_post_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='source_title',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Название источника'),
        ),
    ]
