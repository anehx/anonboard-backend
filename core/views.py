from core           import serializers, models, filters
from rest_framework import viewsets


class TopicView(viewsets.ModelViewSet):
    '''
    View to display topics
    '''
    queryset         = models.Topic.objects.all()
    serializer_class = serializers.TopicSerializer
    filter_class     = filters.TopicFilter


class ThreadView(viewsets.ModelViewSet):
    '''
    View to display threads
    '''
    queryset         = models.Thread.objects.all()
    serializer_class = serializers.ThreadSerializer
    filter_class     = filters.ThreadFilter

    def perform_create(self, serializer):
        '''
        Saves the thread with the current user assigned
        '''
        serializer.save(user=self.request.anonboard_user)


class CommentView(viewsets.ModelViewSet):
    '''
    View to display comments
    '''
    queryset         = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    filter_class     = filters.CommentFilter

    def perform_create(self, serializer):
        '''
        Saves the comment with the current user assigned
        '''
        serializer.save(user=self.request.anonboard_user)
