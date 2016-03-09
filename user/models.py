import hashlib
from django.db import models


class User(models.Model):
    ip         = models.GenericIPAddressField()
    user_agent = models.TextField(blank=True, null=True)

    @property
    def identifier(self):
        key = '%s;%s' % (self.ip, self.user_agent)
        return hashlib.sha256(key.encode('utf-8')).hexdigest()

    def __str__(self):
        return self.identifier

    class Meta:
        unique_together = ('ip', 'user_agent')
