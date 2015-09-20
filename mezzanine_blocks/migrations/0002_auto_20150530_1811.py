# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_blocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='content_en',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='block',
            name='content_nl',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='block',
            name='title_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='block',
            name='title_nl',
            field=models.CharField(max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='richblock',
            name='content_en',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='richblock',
            name='content_nl',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='richblock',
            name='title_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='richblock',
            name='title_nl',
            field=models.CharField(max_length=500, null=True, verbose_name='Title'),
        ),
    ]
