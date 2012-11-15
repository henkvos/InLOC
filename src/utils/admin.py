from django.contrib import admin
from django.contrib.sessions.models import Session
from django import forms

from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models

from genericadmin.admin import GenericAdminModelAdmin, GenericTabularInline, GenericStackedInline

from loc.models import *
from l10n.models import Language

class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']

class LanguageAdmin(admin.ModelAdmin):  
    model = Language
    
class TitleInline(GenericStackedInline):
    model = Title
    extra = 0
    related_lookup_fields = {
        'generic': [['content_type', 'object_id'],],
    }
    
class DescriptionInline(GenericStackedInline):
    model = Description
    extra = 0
    related_lookup_fields = {
        'generic': [['content_type', 'object_id'],],
    }
    
class AbbreviationInline(GenericStackedInline):
    model = Abbreviation
    extra = 0
    related_lookup_fields = {
        'generic': [['content_type', 'object_id'],],
    }
    
class RightsInline(GenericStackedInline):
    model = Rights
    extra = 0
    related_lookup_fields = {
        'generic': [['content_type', 'object_id'],],
    }

class FurtherInfoInline(GenericStackedInline):
    model = FurtherInfo
    extra = 0
    related_lookup_fields = {
        'generic': [['content_type', 'object_id'],],
    }

class LOCModelAdmin(GenericAdminModelAdmin):
    model = LOCModel
    inlines = [
             TitleInline,
             DescriptionInline,
             AbbreviationInline,
             RightsInline,
             FurtherInfoInline,
             ]

class LOCDefinitionAdmin(LOCModelAdmin):
    model = LOCDefinition
 
class LOCStructureAdmin(LOCModelAdmin):
    model = LOCStructure


admin.site.register(Session, SessionAdmin)
admin.site.register(LOCDefinition, LOCDefinitionAdmin)
admin.site.register(LOCStructure, LOCStructureAdmin)
admin.site.register(Language, LanguageAdmin)