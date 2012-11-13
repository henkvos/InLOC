# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Title'
        db.create_table('loc_title', (
            ('id', self.gf('utils.fields.UUIDField')(auto=True, unique=True, max_length=32, primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.CharField')(max_length=36)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['l10n.Language'])),
            ('value', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('loc', ['Title'])

        # Adding model 'Abbreviation'
        db.create_table('loc_abbreviation', (
            ('id', self.gf('utils.fields.UUIDField')(auto=True, unique=True, max_length=32, primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.CharField')(max_length=36)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['l10n.Language'])),
            ('value', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('loc', ['Abbreviation'])

        # Adding model 'Description'
        db.create_table('loc_description', (
            ('id', self.gf('utils.fields.UUIDField')(auto=True, unique=True, max_length=32, primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.CharField')(max_length=36)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['l10n.Language'])),
            ('value', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('loc', ['Description'])

        # Adding model 'Rights'
        db.create_table('loc_rights', (
            ('id', self.gf('utils.fields.UUIDField')(auto=True, unique=True, max_length=32, primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.CharField')(max_length=36)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['l10n.Language'])),
            ('value', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('loc', ['Rights'])

        # Adding model 'FurtherInfo'
        db.create_table('loc_furtherinfo', (
            ('id', self.gf('utils.fields.UUIDField')(auto=True, unique=True, max_length=32, primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.CharField')(max_length=36)),
            ('info', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('loc', ['FurtherInfo'])

        # Adding model 'LOCStructure'
        db.create_table('loc_locstructure', (
            ('id', self.gf('utils.fields.UUIDField')(auto=True, unique=True, max_length=32, primary_key=True)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['l10n.Language'], null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('issued', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('validity_start', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('validity_end', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('version', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
        ))
        db.send_create_signal('loc', ['LOCStructure'])

        # Adding model 'LOCDefinition'
        db.create_table('loc_locdefinition', (
            ('id', self.gf('utils.fields.UUIDField')(auto=True, unique=True, max_length=32, primary_key=True)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['l10n.Language'], null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('issued', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('validity_start', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('validity_end', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('version', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('primary_structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['loc.LOCStructure'], null=True, blank=True)),
        ))
        db.send_create_signal('loc', ['LOCDefinition'])


    def backwards(self, orm):
        # Deleting model 'Title'
        db.delete_table('loc_title')

        # Deleting model 'Abbreviation'
        db.delete_table('loc_abbreviation')

        # Deleting model 'Description'
        db.delete_table('loc_description')

        # Deleting model 'Rights'
        db.delete_table('loc_rights')

        # Deleting model 'FurtherInfo'
        db.delete_table('loc_furtherinfo')

        # Deleting model 'LOCStructure'
        db.delete_table('loc_locstructure')

        # Deleting model 'LOCDefinition'
        db.delete_table('loc_locdefinition')


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
            'issued': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['l10n.Language']", 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'primary_structure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['loc.LOCStructure']", 'null': 'True', 'blank': 'True'}),
            'validity_end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'validity_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'})
        },
        'loc.locstructure': {
            'Meta': {'object_name': 'LOCStructure'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('utils.fields.UUIDField', [], {'auto': 'True', 'unique': 'True', 'max_length': '32', 'primary_key': 'True'}),
            'issued': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['l10n.Language']", 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'validity_end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'validity_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
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