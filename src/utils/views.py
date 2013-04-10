# -*- coding: utf-8 -*-

import dateutil.parser
from lxml import etree, objectify

from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect
from django.views.generic.base import View

from l10n.models import Language
from loc.models import *
from utils.forms import ImportFileForm

XML_NAMESPACE = "http://www.w3.org/XML/1998/namespace"
INLOC_NAMESPACE = "http://purl.org/net/inloc/"

XML = "{%s}" % XML_NAMESPACE
INLOC = "{%s}" % INLOC_NAMESPACE

NSMAP = {None : INLOC_NAMESPACE} # the default namespace (no prefix)

PROPERTY_LIST = ('title', 'description', 'rights', 'furtherInformation')


def process_properties(xml_node, obj, prop):

    try:
        for p in xml_node.iterchildren(INLOC+prop):

            lang_code = p.get(XML+'lang')
            try:
                lang = Language.objects.get(code=lang_code)
            except:
                lang = None

            property = ContentType.objects.get(app_label='loc', model=prop).model_class()()
            property.content_type = ContentType.objects.get_for_model(obj)
            property.object_id = obj.pk
            property.language = lang
            property.value = p.text

            print p.text

            property.save()

    except Exception as e:
        print '%s (%s)' % (e.message, type(e))


class XMLImportView(View):
    def post(self,request):
        form = ImportFileForm(request.POST, request.FILES)

        if form.is_valid():
            f = request.FILES['file']

            structure = objectify.parse(f)

            #get LOC structure
            root = structure.getroot()

            stru = LOCStructure()
            stru.id = root.get('id')
            if hasattr(root, 'version'):
                stru.version = root.version
            if hasattr(root, 'created'):
                stru.created = dateutil.parser.parse(str(root.created))

            try:
                lang_code = root.get(XML+'lang')
                lang = Language.objects.get(code=lang_code)
                stru.language = lang
            except:
                pass

            stru.save()

            for p in PROPERTY_LIST:
                process_properties(root, stru, p)

            #get LOCdefinitions
            for loc in root.iterchildren(INLOC+'LOCdefinition'):
                locdef = LOCDefinition()
                locdef.primary_structure = stru
                locdef.id = loc.get('id')
                if hasattr(loc, 'version'):
                    locdef.version = loc.version
                if hasattr(loc, 'created'):
                    locdef.created = dateutil.parser.parse(str(loc.created))

                print loc.get('id')

                locdef.save()

                for p in PROPERTY_LIST:
                    process_properties(loc, locdef, p)

            #get LOCassociations
            for loc in root.iterchildren(INLOC+'LOCassociation'):
                print loc.get('type', 'no type')


        return redirect('/')