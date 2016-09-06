# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields
import mezzanine.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('login_required', models.BooleanField(default=False, help_text='If checked, only logged in users can view this page', verbose_name='Login required')),
                ('show_title', models.BooleanField(default=False, help_text='If checked, show block title', verbose_name='Show title')),
                ('content', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Block',
                'verbose_name_plural': 'Blocks',
            },
        ),
        migrations.CreateModel(
            name='BlockCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'verbose_name': 'Block category',
                'verbose_name_plural': 'Block categories',
            },
        ),
        migrations.CreateModel(
            name='ImageBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('login_required', models.BooleanField(default=False, help_text='If checked, only logged in users can view this page', verbose_name='Login required')),
                ('show_title', models.BooleanField(default=False, help_text='If checked, show block title', verbose_name='Show title')),
                ('image', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Image', blank=True)),
                ('description', mezzanine.core.fields.RichTextField(null=True, verbose_name='Description', blank=True)),
                ('url', models.URLField(help_text='Optional URL.', max_length=255, null=True, verbose_name='External URL', blank=True)),
                ('height', models.IntegerField(default=100, help_text='Height in pixels.', verbose_name='Height')),
                ('width', models.IntegerField(default=200, help_text='Width in pixels.', verbose_name='Width')),
                ('quality', models.IntegerField(default=80, verbose_name='Quality')),
                ('category', models.ForeignKey(blank=True, to='mezzanine_blocks.BlockCategory', null=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'verbose_name': 'Image Block',
                'verbose_name_plural': 'Image Blocks',
            },
            bases=(models.Model, mezzanine.utils.models.AdminThumbMixin),
        ),
        migrations.CreateModel(
            name='RichBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('login_required', models.BooleanField(default=False, help_text='If checked, only logged in users can view this page', verbose_name='Login required')),
                ('show_title', models.BooleanField(default=False, help_text='If checked, show block title', verbose_name='Show title')),
                ('category', models.ForeignKey(blank=True, to='mezzanine_blocks.BlockCategory', null=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'verbose_name': 'Rich Block',
                'verbose_name_plural': 'Rich Blocks',
            },
        ),
        migrations.AddField(
            model_name='block',
            name='category',
            field=models.ForeignKey(blank=True, to='mezzanine_blocks.BlockCategory', null=True),
        ),
        migrations.AddField(
            model_name='block',
            name='site',
            field=models.ForeignKey(editable=False, to='sites.Site'),
        ),
    ]
