# -*- coding: utf-8 -*-

from rest_framework import serializers

from loc.models import LOCStructure


class LOCStructureSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField('get_title')

    def get_title(self, obj):
        return obj.loc_title()

    class Meta:
        model = LOCStructure
        fields = ('id', 'title')