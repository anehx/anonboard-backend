from core                    import models
from rest_framework          import serializers
from rest_framework_json_api import relations
from user.models             import User
from user.serializers        import UserSerializer


class TopicSerializer(serializers.ModelSerializer):
    threads = relations.ResourceRelatedField(
        read_only=True,
        many=True
    )

    class Meta:
        model = models.Topic


class ThreadSerializer(serializers.ModelSerializer):
    user = relations.ResourceRelatedField(
        queryset=User.objects.all(),
        required=False
    )

    topic = relations.ResourceRelatedField(
        queryset=models.Topic.objects.all()
    )

    comments = relations.ResourceRelatedField(
        read_only=True,
        many=True
    )

    class Meta:
        model = models.Thread


class CommentSerializer(serializers.ModelSerializer):
    user = relations.ResourceRelatedField(
        queryset=User.objects.all(),
        required=False
    )

    thread = relations.ResourceRelatedField(
        queryset=models.Thread.objects.all()
    )

    class Meta:
        model = models.Comment


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
