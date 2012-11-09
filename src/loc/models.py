from django.db import models
from django.conf import settings
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from l10n.models import Language
from utils.fields import UUIDField

class LOCModel(models.Model):
    '''
    Abstract base class for LOCdefinitions and LOCstructures
    '''
    id = UUIDField(auto=True, primary_key=True)
    language = models.ForeignKey(Language, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True) #multiple titles?
    description = models.TextField(blank=True, null=True) #multiple descriptions?
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True, editable=False)
    issued = models.DateTimeField(blank=True, null=True)
    validity_start = models.DateTimeField(blank=True, null=True)
    validity_end = models.DateTimeField(blank=True, null=True)
    version = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    
    def uri(self):
        '''
        generates uri for LOC
        '''
        base_uri = settings.LOC_BASE_URI
        return u'%s/%s' % (base_uri, self.id)

    class Meta:
        abstract = True
        
class LOCDefinition(LOCModel):
    pass

class FurtherInfo(models.Model):
    id = UUIDField(auto=True, primary_key=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.CharField(max_length=36)
    info = models.TextField(blank=True, null=True)
    