# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-26 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20160926_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='source_link',
            field=models.CharField(default='https://ria.ru/', max_length=100, verbose_name='Ссылка на источник'),
        ),
        migrations.AlterField(
            model_name='post',
            name='source_name',
            field=models.CharField(default='', max_length=100, verbose_name='Название источника'),
        ),
    ]