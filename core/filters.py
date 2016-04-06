from django_filters import FilterSet
from core           import models


class TopicFilter(FilterSet):
    '''
    Class for filtering the topics
    '''
    class Meta:
        '''
        Meta options for topic filter

        Defines the model and its attributes
        which are available for filtering
        '''
        model  = models.Topic
        fields = [ 'identifier' ]


class ThreadFilter(FilterSet):
    '''
    Class for filtering the threads
    '''
    class Meta:
        '''
        Meta options for thread filter

        Defines the model and its attributes
        which are available for filtering
        '''
        model  = models.Thread
        fields = [ 'topic', 'id' ]


class CommentFilter(FilterSet):
    '''
    Class for filtering the comments
    '''
    class Meta:
        '''
        Meta options for comment filter

        Defines the model and its attributes
        which are available for filtering
        '''
        model  = models.Comment
        fields = [ 'thread' ]
