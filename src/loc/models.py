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


class FurtherInformation(LOCProperty):
    class Meta:
        verbose_name_plural = "Further information"
    pass


class LOCModel(models.Model):
    '''
    Abstract base class for LOCdefinitions and LOCstructures
    '''
    pk_id = models.AutoField(primary_key=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    language = models.ForeignKey(Language, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True, editable=False)
    issued = models.DateField(blank=True, null=True)
    validity_start = models.DateField(blank=True, null=True)
    validity_end = models.DateField(blank=True, null=True)
    version = models.CharField(max_length=32, blank=True, null=True)
    
    description = generic.GenericRelation(Description)
    title = generic.GenericRelation(Title)
    abbr = generic.GenericRelation(Abbreviation)
    further_information = generic.GenericRelation(FurtherInformation)
    rights = generic.GenericRelation(Rights)
    
    def uri(self):
        '''
        generates uri for LOC
        '''
        base_uri = settings.LOC_BASE_URI
        return u'%s%s/%s' % (base_uri, 'api/locstructures', self.pk_id)

    def loc_title(self):
        try:
            en = Language.objects.get(code='en')
            en_title = self.title.get(language=en)
            if en_title:
                return u'%s' % (en_title)
            else:
                return u'%s' % (' - no title - ')

        except:
            titles = Title.objects.filter(object_id=self.pk_id).exclude(language__isnull=False)
            try:
                title = titles[0]
                return u'%s' % (title)
            except:
                return u'%s' % (' - no title - ')

    def loc_description(self):
        try:
            en = Language.objects.get(code='en')
            en_description = self.description.get(language=en)
            if en_description:
                return u'%s' % (en_description)
            else:
                return u'%s' % (' - no description - ')

        except:
            descriptions = Description.objects.filter(object_id=self.pk_id).exclude(language__isnull=False)
            try:
                description = descriptions[0]
                return u'%s' % (description)
            except:
                return u'%s' % (' - description - ')
    
    def __unicode__(self):
        return self.loc_title()

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
    primary_structure = models.ForeignKey(LOCStructure, blank=True, null=True, related_name='locdefinitions')

    def uri(self):
        '''
        generates uri for LOC
        '''
        base_uri = settings.LOC_BASE_URI
        return u'%s%s/%s' % (base_uri, 'api/locdefinitions', self.pk_id)


class Label(LOCProperty):
    pass


class LOCAssociationRelatedBase(models.Model):
    pk_id = models.AutoField(primary_key=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    label = generic.GenericRelation(Label)

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'%s (%s)' % (self.id, self.label)


class LOCAssociationObject(LOCAssociationRelatedBase):
    pass


class LOCAssociationSubject(LOCAssociationRelatedBase):
    pass


class LOCAssociationScheme(LOCAssociationRelatedBase):
    pass


class LOCAssociation(models.Model):
    '''
    see http://wiki.teria.no/display/inloc/type
    '''
    TYPE_CHOICES = (
        ('LOCrel','http://purl.org/net/inloc/LOCrel'),
        ('by','http://purl.org/net/inloc/by'),
        ('category','http://purl.org/net/inloc/category'),
        ('credit','http://purl.org/net/inloc/credit'),
        ('level','http://purl.org/net/inloc/level'),
        ('topic','http://purl.org/net/inloc/topic'),
    )
    pk_id = models.AutoField(primary_key=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    number = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    object = models.ForeignKey(LOCAssociationObject)
    subject = models.ForeignKey(LOCAssociationSubject)
    scheme = models.ForeignKey(LOCAssociationScheme)
    type = models.CharField(max_length=64, choices=TYPE_CHOICES)


    def __unicode__(self):
        return u'%s (%s)' % (self.subject, self.type)