from django.contrib import admin

from .models import Post, Category


class PostFields(admin.ModelAdmin):
    list_display = ('title', 'category', 'published', 'date_created', 'date_of_change')
admin.site.register(Post, PostFields)


class CategoryFields(admin.ModelAdmin):
    list_display = ('name', 'pk')
admin.site.register(Category, CategoryFields)