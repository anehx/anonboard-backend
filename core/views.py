from core           import serializers, models, filters
from rest_framework import viewsets


class TopicView(viewsets.ModelViewSet):
    queryset         = models.Topic.objects.all()
    serializer_class = serializers.TopicSerializer
    filter_class     = filters.TopicFilter


class ThreadView(viewsets.ModelViewSet):
    queryset         = models.Thread.objects.all()
    serializer_class = serializers.ThreadSerializer
    filter_class     = filters.ThreadFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.anonboard_user)


class CommentView(viewsets.ModelViewSet):
    queryset         = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    filter_class     = filters.CommentFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.anonboard_user)
