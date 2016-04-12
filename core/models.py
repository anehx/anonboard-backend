from django.db            import models
from django.utils         import timezone
from user.models          import User
from adminsortable.models import SortableMixin


class Topic(SortableMixin):
    '''
    Model to define the behaviour of a topic
    '''
    class Meta:
        '''
        Meta options for topic model

        Defines the default ordering
        '''
        ordering = [ 'order' ]

    name        = models.CharField(max_length=50, unique=True)
    identifier  = models.SlugField(max_length=50, unique=True)
    description = models.CharField(max_length=255)

    order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True
    )

    @property
    def threads_last_day(self):
        '''
        Counts the amount of threads in this topic
        created in the last 24 hours

        :return: The amount of threads
        :rtype:  int
        '''
        last_day = timezone.now() - timezone.timedelta(days=1)

        return len(Thread.objects.filter(topic=self, created__gte=last_day))

    def __str__(self):
        '''
        Represents a topic as a string

        :return: The name of the topic
        :rtype:  str
        '''
        return self.name


class Thread(models.Model):
    '''
    Model to define the behaviour of a thread

    Is related to a topic
    '''
    class Meta:
        '''
        Meta options for thread model

        Defines the default ordering
        '''
        ordering = [ '-created' ]

    user    = models.ForeignKey(User)
    topic   = models.ForeignKey(Topic, related_name='threads')
    title   = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''
        Represents a thread as a string

        :return: The title of the thread
        :rtype:  str
        '''
        return self.title


class Comment(models.Model):
    '''
    Model to define the behaviour of a comment

    Is related to a user and a thread
    '''
    class Meta:
        '''
        Meta options for comment model

        Defines the default ordering
        '''
        ordering = [ '-created' ]

    user       = models.ForeignKey(User)
    thread     = models.ForeignKey(Thread, related_name='comments')
    content    = models.TextField()
    created    = models.DateTimeField(auto_now_add=True)
    referenced = models.ManyToManyField('Comment', null=True, blank=True)

    def __str__(self):
        '''
        Represents a comment as a string

        :return: The user identifier and the thread title
        :rtype:  str
        '''
        return 'Comment from %s to thread %s' % (
            str(self.user),
            str(self.thread)
        )
