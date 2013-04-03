# -*- coding: utf-8 -*-

from rest_framework import generics

from l10n.models import Language
from l10n.serializers import LanguageSerializer

class LanguageList(generics.ListAPIView):
    model = Language
    serializer_class = LanguageSerializer