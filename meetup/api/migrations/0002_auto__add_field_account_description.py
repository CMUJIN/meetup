# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Account.description'
        db.add_column(u'api_account', 'description',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Account.description'
        db.delete_column(u'api_account', 'description')


    models = {
        u'api.account': {
            'Meta': {'object_name': 'Account'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'gender': ('django.db.models.fields.BooleanField', [], {}),
            'last_modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'orientation': ('django.db.models.fields.BooleanField', [], {}),
            'photo_link1': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'photo_link2': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'photo_link3': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'photo_link4': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'photo_link5': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'photo_link6': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'user_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'api.location': {
            'Meta': {'object_name': 'Location'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'user_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'api.match': {
            'Meta': {'object_name': 'Match'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'islike': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'match_user_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'user_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['api']