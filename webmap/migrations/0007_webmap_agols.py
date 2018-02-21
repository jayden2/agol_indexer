# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-21 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agol', '0004_auto_20170313_1709'),
        ('webmap', '0006_webmap_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='webmap',
            name='agols',
            field=models.ManyToManyField(related_name='webmaps', related_query_name='agol', to='agol.AGOL_Item'),
        ),
    ]
