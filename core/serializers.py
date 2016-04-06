from core                    import models
from rest_framework          import serializers
from rest_framework_json_api import relations
from user.models             import User
from user.serializers        import UserSerializer


class TopicSerializer(serializers.ModelSerializer):
    '''
    Serializer to define how to represent
    topics in the API
    '''
    class Meta:
        '''
        Meta options for topic serializer

        Defines which model to represent and
        which fields to display
        '''
        model  = models.Topic
        fields = (
            'name',
            'identifier',
            'description',
            'threads_last_day',
            'threads',
        )

    threads = relations.ResourceRelatedField(
        read_only=True,
        many=True
    )


class ThreadSerializer(serializers.ModelSerializer):
    '''
    Serializer to define how to represent
    threads in the API
    '''
    class Meta:
        '''
        Meta options for thread serializer

        Defines which model to represent and
        which fields to display
        '''
        model  = models.Thread
        fields = (
            'title',
            'content',
            'created',
            'user',
            'topic',
            'comments',
        )

    user = relations.ResourceRelatedField(
        queryset=User.objects.all(),
        allow_null=True,
        required=False
    )

    topic = relations.ResourceRelatedField(
        queryset=models.Topic.objects.all()
    )

    comments = relations.ResourceRelatedField(
        read_only=True,
        many=True
    )


class CommentSerializer(serializers.ModelSerializer):
    '''
    Serializer to define how to represent
    comments in the API
    '''
    class Meta:
        '''
        Meta options for comment serializer

        Defines which model to represent and
        which fields to display
        '''
        model  = models.Comment
        fields = (
            'content',
            'created',
            'user',
            'thread',
        )

    user = relations.ResourceRelatedField(
        queryset=User.objects.all(),
        allow_null=True,
        required=False
    )

    thread = relations.ResourceRelatedField(
        queryset=models.Thread.objects.all()
    )


TopicSerializer.included_serializers = {
    'threads': ThreadSerializer
}

ThreadSerializer.included_serializers = {
    'user':     UserSerializer,
    'topic':    TopicSerializer,
    'comments': CommentSerializer
}

CommentSerializer.included_serializers = {
    'user':     UserSerializer,
    'thread':   ThreadSerializer
}
