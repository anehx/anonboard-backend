import factory

from core           import models
from user.factories import UserFactory


class TopicFactory(factory.django.DjangoModelFactory):
    name        = factory.Faker('text', max_nb_chars=50)
    identifier  = factory.Faker('slug')
    description = factory.Faker('sentence')

    class Meta:
        model = models.Topic


class ThreadFactory(factory.django.DjangoModelFactory):
    user    = factory.SubFactory(UserFactory)
    topic   = factory.SubFactory(TopicFactory)
    title   = factory.Faker('text', max_nb_chars=50)
    content = factory.Faker('text')
    created = factory.Faker('date_time')

    class Meta:
        model = models.Thread


class CommentFactory(factory.django.DjangoModelFactory):
    user    = factory.SubFactory(UserFactory)
    thread  = factory.SubFactory(ThreadFactory)
    content = factory.Faker('text')
    created = factory.Faker('date_time')

    class Meta:
        model = models.Comment
