from core                    import models
from rest_framework          import serializers
from rest_framework_json_api import relations
from user.models             import User
from user.serializers        import UserSerializer


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Topic


class ThreadSerializer(serializers.ModelSerializer):
    user  = relations.ResourceRelatedField(queryset=User.objects.all())
    topic = relations.ResourceRelatedField(queryset=models.Topic.objects.all())

    included_serializers = {
        'user': UserSerializer
    }

    class Meta:
        model = models.Thread


class CommentSerializer(serializers.ModelSerializer):
    user   = relations.ResourceRelatedField(queryset=User.objects.all())
    thread = relations.ResourceRelatedField(queryset=models.Thread.objects.all())

    included_serializers = {
        'user':   UserSerializer,
        'thread': ThreadSerializer
    }

    class Meta:
        model = models.Comment
