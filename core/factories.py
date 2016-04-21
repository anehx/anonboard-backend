import factory

from core           import models
from user.factories import UserFactory


class TopicFactory(factory.django.DjangoModelFactory):
    '''
    Factory for generating test topics
    '''
    class Meta:
        '''
        Meta options for the thread factory

        Defines the django model to generate
        '''
        model = models.Topic

    name        = factory.Faker('uuid4')
    identifier  = factory.Faker('uuid4')
    description = factory.Faker('sentence')


class ThreadFactory(factory.django.DjangoModelFactory):
    '''
    Factory for generating test threads
    '''
    class Meta:
        '''
        Meta options for the comment factory

        Defines the django model to generate
        '''
        model = models.Thread

    user    = factory.SubFactory(UserFactory)
    topic   = factory.SubFactory(TopicFactory)
    title   = factory.Faker('text', max_nb_chars=50)
    content = factory.Faker('text', max_nb_chars=140)


class CommentFactory(factory.django.DjangoModelFactory):
    '''
    Factory for generating test comments
    '''
    class Meta:
        '''
        Meta options for the comment factory

        Defines the django model to generate
        '''
        model = models.Comment

    user    = factory.SubFactory(UserFactory)
    thread  = factory.SubFactory(ThreadFactory)
    content = factory.Faker('text')
