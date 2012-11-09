from django.db import models

class Language(models.Model):
    code = models.CharField(primary_key=True, max_length=32) #e.g. en-gb, en-us, en-au, nl-nl, nl-nl, pt-pt, pt-br
    en_name = models.CharField(max_length=255)
    loc_name = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s: %s ( %s )' % (self.lcid, self.loc_name, self.en_name)