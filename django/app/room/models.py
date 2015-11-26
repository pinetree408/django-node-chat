from django.db import models


class Room(models.Model):

    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(u"created at", auto_now_add=True)

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return "%s" % (self.name,)
