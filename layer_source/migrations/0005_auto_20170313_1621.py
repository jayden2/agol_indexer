# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 08:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('layer_source', '0004_auto_20170215_1400'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='layer_source',
            options={'ordering': ['name'], 'verbose_name': 'Layer Source'},
        ),
        migrations.AlterModelOptions(
            name='layer_source_format',
            options={'ordering': ['formats'], 'verbose_name': 'Layer Source Format'},
        ),
        migrations.AlterModelOptions(
            name='layer_source_format_type',
            options={'ordering': ['format_type'], 'verbose_name': 'Layer Source Feature Type'},
        ),
    ]