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




def process_properties(xml_node, obj, prop):
    print INLOC+prop
    try:
        for p in xml_node.iter(INLOC+prop):

            lang_code = p.get(XML+'lang')
            try:
                lang = Language.objects.get(code=lang_code)
            except:
                lang = None

            property = ContentType.objects.get(app_label='loc', model=prop).model_class()()
            property.content_type = ContentType.objects.get_for_model(obj)
            property.object_id = obj.pk
            property.language = lang
            property.value = p

            property.save()

    except Exception as e:
        print '%s (%s)' % (e.message, type(e))



class XMLImportView(View):
    def post(self,request):
        form = ImportFileForm(request.POST, request.FILES)

        if form.is_valid():
            f = request.FILES['file']

            structure = objectify.parse(f)
            root = structure.getroot()

            stru = LOCStructure()
            stru.id = root.get('id')
            stru.version = root.version
            stru.created = dateutil.parser.parse(str(root.created))

            try:
                lang_code = root.get(XML+'lang')
                lang = Language.objects.get(code=lang_code)
                stru.language = lang
            except:
                pass

            stru.save()

            process_properties(root, stru, 'title')


            '''
            #get title attributres
            try:
                for t in structure.iter(INLOC+'title'):
                    print t
                    lang_code = t.get(XML+'lang')
                    try:
                        lang = Language.objects.get(code=lang_code)
                    except:
                        lang = None

                    title = Title()
                    title.content_type = ContentType.objects.get_for_model(stru)
                    title.object_id = stru.pk
                    title.language = lang
                    title.value = t

                    title.save()

            except:
                pass
            '''

        return redirect('/')


'''
content_type = models.ForeignKey(ContentType)
    object_id = models.CharField(max_length=36)
    language = models.ForeignKey(Language, blank=True, null=True)
    value = models.TextField(blank=True, null=True)


pk_id = models.AutoField(primary_key=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    language = models.ForeignKey(Language, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True, editable=False)
    issued = models.DateField(blank=True, null=True)
    validity_start = models.DateField(blank=True, null=True)
    validity_end = models.DateField(blank=True, null=True)
    version = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)

    description = generic.GenericRelation(Description)
    title = generic.GenericRelation(Title)
    abbr = generic.GenericRelation(Abbreviation)
    further_information = generic.GenericRelation(FurtherInfo)
    rights = generic.GenericRelation(Rights)

'''