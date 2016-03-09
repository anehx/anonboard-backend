from rest_framework import viewsets
from user           import serializers, models, filters


class UserView(viewsets.ModelViewSet):
    queryset         = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_class     = filters.UserFilter
