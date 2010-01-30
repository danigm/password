from django.db import models
from django.utils.translation import ugettext as _

class Site(models.Model):
    siteurl = models.URLField(_('site url'))
    username = models.CharField(_('user name'), max_length=100)
    password = models.CharField(_('password'), max_length=100)
    other = models.CharField(_('comment'), max_length=500, blank=True)
    work = models.IntegerField(default=0)
    notwork = models.IntegerField(default=0)

    def __unicode__(self):
        return "<%s - %s:%s>" % (self.siteurl, self.username, self.password)
