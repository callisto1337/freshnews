# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length = 100, verbose_name=('Посты'))
    preview = models.TextField(max_length = 200, default='')
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=('Дата создания'))
    date_of_change = models.DateTimeField(auto_now=True, verbose_name=('Последнее изменение'))
    image_post = models.ImageField(upload_to='media/', blank=True, null=True)
    interesting = models.BooleanField(default=False, verbose_name=('Интересный'))

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title