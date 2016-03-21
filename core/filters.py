import django_filters

from core import models


class TopicFilter(django_filters.FilterSet):
    class Meta:
        model  = models.Topic
        fields = [ 'identifier' ]


class ThreadFilter(django_filters.FilterSet):
    class Meta:
        model  = models.Thread
        fields = [ 'topic', 'id' ]


class CommentFilter(django_filters.FilterSet):
    class Meta:
        model  = models.Comment
        fields = [ 'thread' ]
