from django.contrib import admin
from django.contrib.sessions.models import Session
from django import forms

from loc.models import LOCDefinition

class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
    

class LOCDefinitionAdmin(admin.ModelAdmin):
    model = LOCDefinition
    



admin.site.register(Session, SessionAdmin)
admin.site.register(LOCDefinition, LOCDefinitionAdmin)