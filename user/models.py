import hashlib
from django.db import models


class User(models.Model):
    ip         = models.GenericIPAddressField(unique=True)
    user_agent = models.TextField(blank=True, null=True)

    @property
    def identification(self):
        key = '%s;%s' % (self.ip, self.user_agent)
        return hashlib.sha256(key.encode('utf-8')).hexdigest()

    def __str__(self):
        return self.identification
