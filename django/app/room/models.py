from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):

    name = models.CharField(max_length=200)
    creator = models.ForeignKey(User)
    created_at = models.DateTimeField(u"created at", auto_now_add=True)

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return "%s" % (self.name,)
