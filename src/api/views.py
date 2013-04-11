# -*- coding: utf-8 -*-

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse, reverse_lazy
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of the InLOC API for Rapasso.
    """
    return Response({
        '/languages': reverse('language-list', request=request),
        '/locstructures': reverse('locstructure-list', request=request),
        })
