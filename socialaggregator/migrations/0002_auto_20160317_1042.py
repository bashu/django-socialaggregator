# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import datetime
import socialaggregator.models


class Migration(migrations.Migration):

    dependencies = [
        ('socialaggregator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ressource',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 17, 10, 42, 42, 419475), verbose_name='creation date', editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ressource',
            name='image',
            field=filer.fields.image.FilerImageField(related_name='edsa_ressource_image', default=None, validators=[socialaggregator.models.validate_image_size], to='filer.Image', blank=True, null=True, verbose_name='image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ressource',
            name='thumbnail',
            field=filer.fields.image.FilerImageField(related_name='edsa_ressource_thumbnail', default=None, blank=True, to='filer.Image', null=True, verbose_name='thumbnail'),
            preserve_default=True,
        ),
    ]
