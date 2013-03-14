# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models

from l10n.models import Language


class LOCProperty(models.Model):
    '''
    Abstract base class for properties on LOC class
    '''
    pk_id = models.AutoField(primary_key=True)
    #id = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.CharField(max_length=36)
    language = models.ForeignKey(Language, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        if self.language:
            lang = self.language.code
            return u'%s: %s' % (lang, self.value)
        else:
            return u'%s' % (self.value)

    
    class Meta:
        abstract = True


class Title(LOCProperty):
    pass


class Abbreviation(LOCProperty):
    pass


class Description(LOCProperty):
    pass


class Rights(LOCProperty):
    class Meta:
        verbose_name_plural = "Rights"
    pass


class FurtherInfo(models.Model):
    pk_id = models.AutoField(primary_key=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.CharField(max_length=36)
    info = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return u'%s' % (self.info)
    
    class Meta:
        verbose_name_plural = "Further information"


class LOCModel(models.Model):
    '''
    Abstract base class for LOCdefinitions and LOCstructures
    '''
    pk_id = models.AutoField(primary_key=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    language = models.ForeignKey(Language, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True, editable=False)
    issued = models.DateField(blank=True, null=True)
    validity_start = models.DateField(blank=True, null=True)
    validity_end = models.DateField(blank=True, null=True)
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
    
    def __unicode__(self):
        try:
            en = Language.objects.get(code='en')
            en_title = self.title.get(language=en)
            if en_title:
                return u'%s (%s)' % (en_title, self.id)
            else:
                return u'%s (%s)' % (' - no title - ', self.id)

        except:
            titles = Title.objects.filter(object_id=self.pk_id).exclude(language__isnull=False)
            try:
                title = titles[0]
                return u'%s (%s)' % (title, self.id)
            except:
                return u'%s (%s)' % (' - no title - ', self.id)

    class Meta:
        abstract = True
        

class LOCStructure(LOCModel):
    '''
    A LOCstructure instance shall not have more than one combinationRules property in each (or no specified) language.
    '''
    pass


class CombinationRule(models.Model): #simply a text field instruction
    pk_id = models.AutoField(primary_key=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    loc_structure = models.ForeignKey(LOCStructure)
    language = models.ForeignKey(Language)
    value = models.TextField(blank=True, null=True)


class LOCDefinition(LOCModel):
    '''
    A LOCdefinition instance shall not have more than one primaryStructure property.
    '''
    primary_structure = models.ForeignKey(LOCStructure, blank=True, null=True)


class LOCAssociation():
    pass
    


    