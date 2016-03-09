import factory

from user import models


class UserFactory(factory.django.DjangoModelFactory):
    ip         = factory.Faker('ipv4')
    user_agent = factory.Faker('user_agent')

    class Meta:
        model = models.User
