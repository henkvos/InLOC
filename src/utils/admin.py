# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.sessions.models import Session

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
    model = FurtherInformation
    extra = 0
    related_lookup_fields = {
        'generic': [['content_type', 'object_id'],],
    }


class ExtraIDInline(GenericStackedInline):
    model = ExtraID
    extra = 0
    related_lookup_fields = {
        'generic': [['content_type', 'object_id'],],
        }


class ModificationInline(GenericStackedInline):
    model = Modification
    extra = 0
    related_lookup_fields = {
        'generic': [['content_type', 'object_id'],],
        }

class CombinationRuleInline(admin.StackedInline):
    model = CombinationRule
    extra = 0


class LOCDefinitionAdmin(GenericAdminModelAdmin):
    model = LOCDefinition
    inlines = [
        TitleInline,
        DescriptionInline,
        AbbreviationInline,
        RightsInline,
        FurtherInfoInline,
        ExtraIDInline,
        ModificationInline
    ]

    list_display = ('loc_title', 'loc_description', 'primary_structure')
    #search_fields = ['user__username', 'user__first_name', 'user__last_name',]
    save_as = True
    list_filter = ('primary_structure', 'language')



class LOCStructureAdmin(GenericAdminModelAdmin):
    model = LOCStructure
    inlines = [
        TitleInline,
        DescriptionInline,
        AbbreviationInline,
        RightsInline,
        FurtherInfoInline,
        ExtraIDInline,
        ModificationInline,
        CombinationRuleInline
    ]
    list_filter = ('language',)


class LabelInline(admin.StackedInline):
    model = Label
    extra = 0


class LOCAssociationAdmin(admin.ModelAdmin):
    model = LOCAssociation
    inlines = [
        LabelInline,
    ]
    list_display = ('subject_id', 'type', 'loc_structure')
    list_filter = ('loc_structure', 'type')


admin.site.register(Language, LanguageAdmin)
admin.site.register(LOCDefinition, LOCDefinitionAdmin)
admin.site.register(LOCStructure, LOCStructureAdmin)
admin.site.register(LOCAssociation, LOCAssociationAdmin)
admin.site.register(Session, SessionAdmin)
