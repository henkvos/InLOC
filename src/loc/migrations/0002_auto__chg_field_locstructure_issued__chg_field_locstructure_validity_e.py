# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'LOCStructure.issued'
        db.alter_column('loc_locstructure', 'issued', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'LOCStructure.validity_end'
        db.alter_column('loc_locstructure', 'validity_end', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'LOCStructure.validity_start'
        db.alter_column('loc_locstructure', 'validity_start', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'LOCDefinition.issued'
        db.alter_column('loc_locdefinition', 'issued', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'LOCDefinition.validity_end'
        db.alter_column('loc_locdefinition', 'validity_end', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'LOCDefinition.validity_start'
        db.alter_column('loc_locdefinition', 'validity_start', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):

        # Changing field 'LOCStructure.issued'
        db.alter_column('loc_locstructure', 'issued', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'LOCStructure.validity_end'
        db.alter_column('loc_locstructure', 'validity_end', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'LOCStructure.validity_start'
        db.alter_column('loc_locstructure', 'validity_start', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'LOCDefinition.issued'
        db.alter_column('loc_locdefinition', 'issued', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'LOCDefinition.validity_end'
        db.alter_column('loc_locdefinition', 'validity_end', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'LOCDefinition.validity_start'
        db.alter_column('loc_locdefinition', 'validity_start', self.gf('django.db.models.fields.DateTimeField')(null=True))

    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'l10n.language': {
            'Meta': {'object_name': 'Language'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '32', 'primary_key': 'True'}),
            'en_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'loc_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'loc.abbreviation': {
            'Meta': {'object_name': 'Abbreviation'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('utils.fields.UUIDField', [], {'auto': 'True', 'unique': 'True', 'max_length': '32', 'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['l10n.Language']"}),
            'object_id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'loc.description': {
            'Meta': {'object_name': 'Description'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('utils.fields.UUIDField', [], {'auto': 'True', 'unique': 'True', 'max_length': '32', 'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['l10n.Language']"}),
            'object_id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'loc.furtherinfo': {
            'Meta': {'object_name': 'FurtherInfo'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('utils.fields.UUIDField', [], {'auto': 'True', 'unique': 'True', 'max_length': '32', 'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.CharField', [], {'max_length': '36'})
        },
        'loc.locdefinition': {
            'Meta': {'object_name': 'LOCDefinition'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('utils.fields.UUIDField', [], {'auto': 'True', 'unique': 'True', 'max_length': '32', 'primary_key': 'True'}),
            'issued': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['l10n.Language']", 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'primary_structure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['loc.LOCStructure']", 'null': 'True', 'blank': 'True'}),
            'validity_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'validity_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'})
        },
        'loc.locstructure': {
            'Meta': {'object_name': 'LOCStructure'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('utils.fields.UUIDField', [], {'auto': 'True', 'unique': 'True', 'max_length': '32', 'primary_key': 'True'}),
            'issued': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['l10n.Language']", 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'validity_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'validity_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'})
        },
        'loc.rights': {
            'Meta': {'object_name': 'Rights'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('utils.fields.UUIDField', [], {'auto': 'True', 'unique': 'True', 'max_length': '32', 'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['l10n.Language']"}),
            'object_id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'loc.title': {
            'Meta': {'object_name': 'Title'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('utils.fields.UUIDField', [], {'auto': 'True', 'unique': 'True', 'max_length': '32', 'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['l10n.Language']"}),
            'object_id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['loc']