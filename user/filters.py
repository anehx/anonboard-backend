import django_filters

from user import models

class UserFilter(django_filters.FilterSet):
    class Meta:
        model  = models.User
