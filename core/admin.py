from django.contrib      import admin
from core                import models
from adminsortable.admin import SortableAdmin


@admin.register(models.Topic)
class TopicAdmin(SortableAdmin):
    '''
    Admin interface for topics
    '''
    list_display        = [ 'name', 'identifier' ]
    prepopulated_fields = { 'identifier': ( 'name', ) }


@admin.register(models.Thread)
class ThreadAdmin(admin.ModelAdmin):
    '''
    Admin interface for threads
    '''
    list_display = [ 'title', 'topic' ]


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    '''
    Admin interface for comments
    '''
    list_display = [ 'content' ]
