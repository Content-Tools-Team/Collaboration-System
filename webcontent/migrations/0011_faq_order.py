# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-25 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcontent', '0010_remove_faq_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='order',
            field=models.FloatField(null=True),
        ),
    ]