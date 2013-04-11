# -*- coding: utf-8 -*-

from rest_framework import generics

from loc.models import LOCStructure
from loc.serializers import LOCStructureListSerializer, LOCStructureDetailSerializer


class LOCStructureList(generics.ListAPIView):
    model = LOCStructure
    serializer_class = LOCStructureListSerializer


class LOCStructureDetail(generics.RetrieveUpdateDestroyAPIView):
    model = LOCStructure
    serializer_class = LOCStructureDetailSerializer




'''


def get(self, request, pk=None):
        if pk:
            profile = UserProfile.objects.get(user_id=pk)
        else:
            profile = UserProfile.objects.get(user_id=request.user.id)

        serializer = UserProfileDetailSerializer(profile)
        return Response(serializer.data)


'''