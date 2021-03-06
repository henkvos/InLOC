# -*- coding: utf-8 -*-

import dateutil.parser
from lxml import objectify

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

PROPERTY_LIST = ('title', 'description', 'rights', 'furtherInformation', 'abbr', 'extraID')
PROPERTY_DICT = {
    'title':'title',
    'description':'description',
    'rights':'rights',
    'furtherInformation':'furtherinformation',
    'abbr':'abbreviation',
    'extraID':'extraid',
    'label':'label'
}

def process_modifications(xml_node, obj):
    for node in xml_node.iterchildren(INLOC+'modified'):
        try:
            modification = Modification()
            modification.content_type = ContentType.objects.get_for_model(obj)
            modification.object_id = obj.pk
            modification.date = node.text

            modification.save()

        except Exception as e:
            print '%s (%s)' % (e.message, type(e))


def process_combination_rules(xml_node, obj):
    for node in xml_node.iterchildren(INLOC+'combinationRules'):
        try:
            rule = CombinationRule()
            rule.loc_structure = obj
            lang_code = node.get(XML+'lang')
            try:
                lang = Language.objects.get(code=lang_code)
            except:
                lang = None
            rule.language = lang
            rule.value = node.text

            rule.save()

        except Exception as e:
            print '%s (%s)' % (e.message, type(e))


def process_properties(xml_node, obj, prop):
    try:
        for p in xml_node.iterchildren(INLOC+prop):

            model = PROPERTY_DICT[prop]

            property = ContentType.objects.get(app_label='loc', model=model).model_class()()
            property.content_type = ContentType.objects.get_for_model(obj)
            property.object_id = obj.pk

            if model == 'extraid':
                property.id = p.text
            else:
                lang_code = p.get(XML+'lang')
                try:
                    lang = Language.objects.get(code=lang_code)
                except:
                    lang = None
                property.language = lang
                property.value = p.text

            property.save()

    except Exception as e:
        print '%s (%s)' % (e.message, type(e))


def process_labels(node, locass, for_node):
    try:
        for lbl in node.iterchildren(INLOC+'label'):
            lang_code = lbl.get(XML+'lang')
            try:
                lang = Language.objects.get(code=lang_code)
            except:
                lang = None
            label = Label()
            label.loc_association = locass
            label.language = lang
            label.label_for = for_node
            label.value = lbl.text

            label.save()

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
            if hasattr(root, 'issued'):
                stru.issued = dateutil.parser.parse(str(root.issued))
            if hasattr(root, 'validityStart'):
                stru.validity_start = dateutil.parser.parse(str(root.validityStart))
            if hasattr(root, 'validityEnd'):
                stru.validity_end = dateutil.parser.parse(str(root.validityEnd))

            try:
                lang_code = root.get(XML+'lang')
                lang = Language.objects.get(code=lang_code)
                stru.language = lang
            except:
                pass

            stru.save()

            for p in PROPERTY_LIST:
                process_properties(root, stru, p)

            process_modifications(root, stru)
            process_combination_rules(root, stru)


            #get LOCdefinitions
            for loc in root.iterchildren(INLOC+'LOCdefinition'):
                locdef = LOCDefinition()
                locdef.primary_structure = stru
                locdef.id = loc.get('id')
                if hasattr(loc, 'version'):
                    locdef.version = loc.version
                if hasattr(loc, 'created'):
                    locdef.created = dateutil.parser.parse(str(loc.created))

                locdef.save()

                for p in PROPERTY_LIST:
                    process_properties(loc, locdef, p)

                process_modifications(loc, locdef)


            #get LOCassociations
            for loc in root.iterchildren(INLOC+'LOCassociation'):
                locass = LOCAssociation()
                locass.loc_structure = stru
                locass.type = loc.get('type')
                locass.subject_id = loc.subject.get('id')
                locass.scheme_id = loc.scheme.get('id', '')
                locass.object_id = loc.object.get('id','')
                if hasattr(loc, 'number'):
                    locass.number = loc.number

                locass.save()

                process_labels(loc.scheme, locass, 'scheme')
                process_labels(loc.object, locass, 'object')


        return redirect('/')