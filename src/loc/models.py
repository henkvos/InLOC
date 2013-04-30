# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.template.defaultfilters import truncatewords
from django.utils.translation import ugettext_lazy as _

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


class ExtraID(models.Model):
    pk_id = models.AutoField(primary_key=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.CharField(max_length=36)
    id = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.id

class Modification(models.Model):
    pk_id = models.AutoField(primary_key=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.CharField(max_length=36)
    date = models.DateTimeField()

    def __unicode__(self):
        return self.date
    

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
        if self.loc_title() == ' - no title - ':
            return truncatewords(self.loc_description(),5)
        else:
            return self.loc_title()

    def loc_search_title(self):
        if self.loc_title() == ' - no title - ':
            return truncatewords(self.loc_description(),5)
        else:
            return self.loc_title()

    class Meta:
        abstract = True
        

class LOCStructure(LOCModel):
    '''
    A LOCstructure instance shall not have more than one combinationRules property in each (or no specified) language.
    '''

    def base_url(self):
        return self.id[:-1]


class CombinationRule(models.Model): #simply a text field instruction
    pk_id = models.AutoField(primary_key=True)
    loc_structure = models.ForeignKey(LOCStructure)
    language = models.ForeignKey(Language, blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    def __unicode__(self):
        if self.language:
            lang = self.language.code
            return u'%s: %s' % (lang, self.value)
        else:
            return u'%s' % (self.value)


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

class LOCAssociation(models.Model):
    '''
    see http://wiki.teria.no/display/inloc/type
    '''
    TYPE_CHOICES = (
        ('http://purl.org/net/inloc/LOCrel', _('LOCrel')),
        ('http://purl.org/net/inloc/by', _('by')),
        ('http://purl.org/net/inloc/category', _('category')),
        ('http://purl.org/net/inloc/credit', _('credit')),
        ('http://purl.org/net/inloc/level', _('level')),
        ('http://purl.org/net/inloc/topic', _('topic'))
    )
    pk_id = models.AutoField(primary_key=True)
    loc_structure = models.ForeignKey(LOCStructure, related_name='locassociations') #this field is added to easily collect all associations for a certain LOCstructure
    type = models.CharField(max_length=64, choices=TYPE_CHOICES)
    subject_id = models.CharField(max_length=255)
    scheme_id = models.CharField(max_length=255, blank=True, null=True)
    object_id = models.CharField(max_length=255, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s (%s)' % (self.subject_id, self.type)


class Label(models.Model):
    FOR_CHOICES = (
        ('subject', _('subject')), #not likely to be used
        ('scheme', _('scheme')),
        ('object', _('object')),
    )
    pk_id = models.AutoField(primary_key=True)
    loc_association = models.ForeignKey(LOCAssociation, related_name='labels')
    label_for = models.CharField(max_length=32, choices=FOR_CHOICES)
    language = models.ForeignKey(Language, blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u'%s: %s' % (self.label_for, self.value)


