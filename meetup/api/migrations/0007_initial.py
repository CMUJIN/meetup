# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Account'
        db.create_table(u'api_account', (
            ('user_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20, db_index=True)),
            ('gender', self.gf('django.db.models.fields.BooleanField')(db_index=True)),
            ('age', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('orientation', self.gf('django.db.models.fields.BooleanField')(db_index=True)),
            ('photo_link1', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('photo_link2', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('photo_link3', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('photo_link4', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('photo_link5', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('photo_link6', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Account'])

        # Adding model 'Location'
        db.create_table(u'api_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(db_index=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(db_index=True)),
            ('last_update_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Location'])

        # Adding model 'Match'
        db.create_table(u'api_match', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('match_user_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('islike', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'api', ['Match'])

        # Adding unique constraint on 'Match', fields ['user_id', 'match_user_id']
        db.create_unique(u'api_match', ['user_id', 'match_user_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Match', fields ['user_id', 'match_user_id']
        db.delete_unique(u'api_match', ['user_id', 'match_user_id'])

        # Deleting model 'Account'
        db.delete_table(u'api_account')

        # Deleting model 'Location'
        db.delete_table(u'api_location')

        # Deleting model 'Match'
        db.delete_table(u'api_match')


    models = {
        u'api.account': {
            'Meta': {'object_name': 'Account'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.BooleanField', [], {'db_index': 'True'}),
            'last_modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'}),
            'orientation': ('django.db.models.fields.BooleanField', [], {'db_index': 'True'}),
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
            'latitude': ('django.db.models.fields.FloatField', [], {'db_index': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'db_index': 'True'}),
            'user_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'api.match': {
            'Meta': {'unique_together': "(('user_id', 'match_user_id'),)", 'object_name': 'Match'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'islike': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'match_user_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'user_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['api']