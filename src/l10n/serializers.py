# -*- coding: utf-8 -*-

from rest_framework.serializers import ModelSerializer

from l10n.models import Language

class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Language