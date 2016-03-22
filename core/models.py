from django.db            import models
from user.models          import User
from adminsortable.models import SortableMixin


class Topic(SortableMixin):
    name        = models.CharField(max_length=50, unique=True)
    identifier  = models.SlugField(max_length=50, unique=True)
    description = models.CharField(max_length=255)

    order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = [ 'order' ]


class Thread(models.Model):
    user    = models.ForeignKey(User)
    topic   = models.ForeignKey(Topic, related_name='threads')
    title   = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = [ 'created' ]


class Comment(models.Model):
    user    = models.ForeignKey(User)
    thread  = models.ForeignKey(Thread, related_name='comments')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment from %s to thread %s' % (
            str(self.user),
            str(self.thread)
        )

    class Meta:
        ordering = [ 'created' ]
