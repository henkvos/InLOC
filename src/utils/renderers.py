# -*- coding: utf-8 -*-

from django.utils.encoding import smart_unicode
from django.utils.xmlutils import SimplerXMLGenerator

from rest_framework import renderers
from rest_framework.compat import StringIO, smart_text, six


class InLOCXMLRenderer(renderers.BaseRenderer):
    """
    Renderer which serializes to inLOC XML.
    """

    media_type = 'application/xml'
    format = 'xml'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders *obj* into serialized XML.
        """
        if data is None:
            return ''

        stream = StringIO()

        xml = SimplerXMLGenerator(stream, "utf-8")
        xml.startDocument()
        xml.startElement("inloc", {})

        self._to_xml(xml, data)

        xml.endElement("inloc")
        xml.endDocument()
        return stream.getvalue()

    def _to_xml(self, xml, data):
        if isinstance(data, (list, tuple)):
            for item in data:
                xml.startElement("list-item", {})
                self._to_xml(xml, item)
                xml.endElement("list-item")

        elif isinstance(data, dict):
            for key, value in six.iteritems(data):
                xml.startElement(key, {})
                self._to_xml(xml, value)
                xml.endElement(key)

        elif data is None:
            # Don't output any value
            pass

        else:
            xml.characters(smart_text(data))