# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-25 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_lab_manuals_reference_material_sample_papers_timetable'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference_material',
            name='Image',
            field=models.ImageField(default='None', upload_to=None),
        ),
    ]
