# -*- coding: utf-8 -*-

from rest_framework import generics

from loc.models import LOCStructure
from loc.serializers import LOCStructureSerializer


class LOCStructureList(generics.ListAPIView):
    model = LOCStructure
    serializer_class = LOCStructureSerializer


