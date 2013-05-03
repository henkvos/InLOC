# -*- coding: utf-8 -*-

from itertools import chain

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from loc.models import LOCStructure, LOCDefinition, Description, Title
from loc.serializers import LOCStructureListSerializer, LOCStructureDetailSerializer, SearchSerializer, LOCSearchSerializer


class LOCStructureList(generics.ListAPIView):
    model = LOCStructure
    serializer_class = LOCStructureListSerializer


class LOCStructureDetail(generics.RetrieveUpdateDestroyAPIView):
    model = LOCStructure
    serializer_class = LOCStructureDetailSerializer


class LOCSearch(APIView):
    """
    Search description and title properties of LOCdefinition and LOCstructures. Used for e.g. type ahead fields or search boxes
    """
    def get(self, request):

        term = request.GET.get('term', None)

        if term:
            descriptions = Description.objects.filter(value__icontains=term)[:10]
            #titles = Title.objects.filter(value__icontains=term)[:10]
            #objects = chain(descriptions, titles)
        else:
            descriptions = Description.objects.all()
            #titles = Title.objects.all()
            #objects = None

        serializer = LOCSearchSerializer(descriptions)
        return Response(serializer.data)


class Search(APIView):
    """
    Search description and title properties of LOCdefinition and LOCstructures. Used for e.g. type ahead fields or search boxes
    """
    def get(self, request):

        query = request.GET.get('query', None)

        if query:
            descriptions = Description.objects.filter(value__icontains=query)[:10]
            #titles = Title.objects.filter(value__icontains=query)[:10]
            #objects = chain(descriptions, titles)
        else:
            descriptions = Description.objects.all()
            #titles = Title.objects.all()
            #objects = None

        serializer = SearchSerializer(descriptions)
        return Response(serializer.data)


class LOCDefitionView(View):
    def get(self, request, id=None):
        locdef = LOCDefinition.objects.get(pk=id)
        return render(request, 'search/locdefinition.html', {"locdef":locdef})


class LOCStructureView(View):
    def get(self, request, id=None):
        print id
        return HttpResponse("OK")


class RdfView(View):
    def get(self, request, id=None):
        locstructure = LOCStructure.objects.get(pk=id)
        print locstructure
        return render(request, 'export/locstucture.rdf.ttl', {"locstructure":locstructure})