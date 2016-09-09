from django.contrib import admin

from .models import Post


class PostFields(admin.ModelAdmin):
    list_display = ('title', 'interesting', 'date_created', 'date_of_change')
admin.site.register(Post, PostFields)