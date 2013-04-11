# -*- coding: utf-8 -*-

from rest_framework import serializers

from loc.models import LOCStructure


class LOCStructureBaseSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField('get_title')
    description = serializers.SerializerMethodField('get_description')
    uri = serializers.SerializerMethodField('get_uri')
    #locdefinitions = serializers.RelatedField(many=True)

    def get_title(self, obj):
        return obj.loc_title()

    def get_description(self, obj):
        return obj.loc_description()

    def get_uri(self, obj):
        return obj.uri()

    class Meta:
        model = LOCStructure


class LOCStructureListSerializer(LOCStructureBaseSerializer):

    class Meta:
        model = LOCStructure
        #fields = ('pk_id', 'id', 'title')
        fields = ('pk_id', 'uri', 'id', 'title')


class LOCStructureDetailSerializer(LOCStructureBaseSerializer):

    class Meta:
        model = LOCStructure