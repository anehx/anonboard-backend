from django.contrib import admin

from core import models


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display        = [ 'name', 'identifier' ]
    prepopulated_fields = { 'identifier': ( 'name', ) }


@admin.register(models.Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = [ 'title' ]


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [ 'content' ]
