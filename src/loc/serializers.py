# -*- coding: utf-8 -*-

from rest_framework import serializers
from django.conf import settings

from loc.models import LOCStructure, LOCDefinition, Description, LOCAssociation, Title, Abbreviation, FurtherInformation, Rights, CombinationRule, Label

LOC_BASE_URI = settings.LOC_BASE_URI


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ('language', 'value', 'label_for')


class LOCAssociationSerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many=True)

    class Meta:
        model = LOCAssociation
        fields = ('type', 'subject_id', 'scheme_id', 'object_id', 'number', 'labels')


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ('language', 'value')


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ('language', 'value')


class AbbreviationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abbreviation
        fields = ('language', 'value')


class FurtherInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FurtherInformation
        fields = ('language', 'value')


class RightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rights
        fields = ('language', 'value')


class CombinationRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CombinationRule
        fields = ('language', 'value')


class LocDefinitionSerializer(serializers.ModelSerializer):
    title = TitleSerializer(many=True)
    description = DescriptionSerializer(many=True)
    abbr = AbbreviationSerializer(many=True)
    further_information = FurtherInformationSerializer(many=True)
    rights = RightsSerializer(many=True)

    class Meta:
        model = LOCDefinition


class LocStructureSerializer(serializers.ModelSerializer):
    title = TitleSerializer(many=True)
    description = DescriptionSerializer(many=True)
    abbr = AbbreviationSerializer(many=True)
    further_information = FurtherInformationSerializer(many=True)
    rights = RightsSerializer(many=True)
    combinationrules = CombinationRuleSerializer(many=True)

    locdefinitions = LocDefinitionSerializer(many=True)
    locassociations = LOCAssociationSerializer(many=True)

    class Meta:
        model = LOCStructure
        #depth = 1


class LOCStructureBaseSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField('get_title')
    description = serializers.SerializerMethodField('get_description')
    uri = serializers.SerializerMethodField('get_uri')
    #locdefinitions = serializers.RelatedField(many=True)
    locassociations = LOCAssociationSerializer(many=True)

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
#class LOCStructureDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = LOCStructure


class SearchSerializer(serializers.Serializer):
    value = serializers.SerializerMethodField('get_value')
    uri = serializers.SerializerMethodField('get_uri')

    def get_value(self, obj):
        return obj.value

    def get_uri(self, obj):
        return LOC_BASE_URI + 'view/' + obj.content_type.model + '/' + obj.object_id + '/'


class LOCSearchSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    label = serializers.SerializerMethodField('get_label')
    value = serializers.SerializerMethodField('get_value')
    uri = serializers.SerializerMethodField('get_uri')

    def get_label(self, obj):
        return obj.value

    def get_value(self, obj):
        return obj.value

    def get_uri(self, obj):
        return LOC_BASE_URI+ obj.content_type.model + '/' + obj.object_id + '/'