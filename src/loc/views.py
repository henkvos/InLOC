# -*- coding: utf-8 -*-

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from loc.models import LOCStructure, Description
from loc.serializers import LOCStructureListSerializer, LOCStructureDetailSerializer, SearchSerializer


class LOCStructureList(generics.ListAPIView):
    model = LOCStructure
    serializer_class = LOCStructureListSerializer


class LOCStructureDetail(generics.RetrieveUpdateDestroyAPIView):
    model = LOCStructure
    serializer_class = LOCStructureDetailSerializer


class LOCSearch(APIView):
    """
    Search description and title properties of LOCdefinition and LOCstructures. Used for e.g. type ahead
    """
    def get(self, request):

        term = request.GET.get('term', None)

        if term:
            descriptions = Description.objects.filter(value__icontains=term)[:15]
        else:
            descriptions = Description.objects.all()

        serializer = SearchSerializer(descriptions)
        return Response(serializer.data)

'''


def get(self, request, pk=None):
        if pk:
            profile = UserProfile.objects.get(user_id=pk)
        else:
            profile = UserProfile.objects.get(user_id=request.user.id)

        serializer = UserProfileDetailSerializer(profile)
        return Response(serializer.data)


'''