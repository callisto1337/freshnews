# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-12 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_remove_post_source_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='source_link',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Ссылка на источник'),
        ),
    ]