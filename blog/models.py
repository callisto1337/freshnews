# -*- coding: utf-8 -*-
from django.db import models
from tinymce.models import HTMLField
from tinymce import models as tinymce_models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=('Категория'))

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name=('Название'))
    preview = models.TextField(max_length=300, verbose_name=('Превью'))
    content = tinymce_models.HTMLField(default='', verbose_name=('Контент'))
    image = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name='Картинка')
    image_description = models.CharField(max_length=150, null=True, blank=True, verbose_name=('Описание картинки'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=('Дата создания'))
    date_of_change = models.DateTimeField(auto_now=True, verbose_name=('Последнее изменение'))
    published = models.BooleanField(default=True, verbose_name=('Опубликован'))
    category = models.ForeignKey(Category, null=True, blank=True, verbose_name=('Категория'))
    source_link = models.CharField(max_length=200, unique=True, null=True, blank=True, verbose_name=('Ссылка на источник'))

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title
