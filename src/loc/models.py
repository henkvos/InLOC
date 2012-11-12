from django.db import models
from django.conf import settings
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from l10n.models import Language
from utils.fields import UUIDField

class LOCProperty(models.Model):
    '''
    Abstract base class for properties on LOC class
    '''
    id = UUIDField(auto=True, primary_key=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.CharField(max_length=36)
    language = models.ForeignKey(Language)
    value = models.TextField(blank=True, null=True)
    
    class Meta:
        abstract = True
        
class Title(LOCProperty):
    pass

class Abbreviation(LOCProperty):
    pass

class Description(LOCProperty):
    pass
        
class Rights(LOCProperty):
    pass

class FurtherInfo(models.Model):
    id = UUIDField(auto=True, primary_key=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.CharField(max_length=36)
    info = models.TextField(blank=True, null=True)


class LOCModel(models.Model):
    '''
    Abstract base class for LOCdefinitions and LOCstructures
    '''
    id = UUIDField(auto=True, primary_key=True)
    language = models.ForeignKey(Language, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True, editable=False)
    issued = models.DateTimeField(blank=True, null=True)
    validity_start = models.DateTimeField(blank=True, null=True)
    validity_end = models.DateTimeField(blank=True, null=True)
    version = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    
    description = generic.GenericRelation(Description)
    title = generic.GenericRelation(Title)
    abbr = generic.GenericRelation(Abbreviation)
    further_information = generic.GenericRelation(FurtherInfo)
    rights = generic.GenericRelation(Rights)
    
    def uri(self):
        '''
        generates uri for LOC
        '''
        base_uri = settings.LOC_BASE_URI
        return u'%s/%s' % (base_uri, self.id)

    class Meta:
        abstract = True
        
        
class LOCStructure(LOCModel):
    '''
    A LOCstructure instance shall not have more than one combinationRules property in each (or no specified) language.
    '''
    pass

class CombinationRule():
    id = UUIDField(auto=True, primary_key=True)
    loc_structure = models.ForeignKey(LOCStructure)
    language = models.ForeignKey(Language)
    value = models.TextField(blank=True, null=True)


class LOCDefinition(LOCModel):
    '''
    A LOCdefinition instance shall not have more than one primaryStructure property.
    '''
    primary_structure = models.ForeignKey(LOCStructure, blank=True, null=True)
    


    