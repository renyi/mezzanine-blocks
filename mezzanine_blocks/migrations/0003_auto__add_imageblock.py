# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ImageBlock'
        db.create_table('mezzanine_blocks_imageblock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mezzanine_blocks.BlockCategory'], null=True, blank=True)),
            ('login_required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('show_title', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('image', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('mezzanine.core.fields.RichTextField')(null=True, blank=True)),
        ))
        db.send_create_signal('mezzanine_blocks', ['ImageBlock'])


    def backwards(self, orm):
        # Deleting model 'ImageBlock'
        db.delete_table('mezzanine_blocks_imageblock')


    models = {
        'mezzanine_blocks.block': {
            'Meta': {'object_name': 'Block'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mezzanine_blocks.BlockCategory']", 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_title': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'mezzanine_blocks.blockcategory': {
            'Meta': {'object_name': 'BlockCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'mezzanine_blocks.imageblock': {
            'Meta': {'object_name': 'ImageBlock'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mezzanine_blocks.BlockCategory']", 'null': 'True', 'blank': 'True'}),
            'description': ('mezzanine.core.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_title': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'mezzanine_blocks.richblock': {
            'Meta': {'object_name': 'RichBlock'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mezzanine_blocks.BlockCategory']", 'null': 'True', 'blank': 'True'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_title': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    try:
        from mptt.models import MPTTModel, TreeForeignKey
        models['mezzanine_blocks.blockcategory']['parent'] =  ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'child'", 'null': 'True', 'to': "orm['mezzanine_blocks.BlockCategory']"})
        models['mezzanine_blocks.blockcategory']['level'] = ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        models['mezzanine_blocks.blockcategory']['lft'] = ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        models['mezzanine_blocks.blockcategory']['rght'] = ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        models['mezzanine_blocks.blockcategory']['tree_id'] = ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
    except ImportError:
        pass

    complete_apps = ['mezzanine_blocks']