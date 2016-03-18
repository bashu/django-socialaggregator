# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import socialaggregator.models
import filer.fields.image
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('filer', '0002_auto_20150606_2003'),
        ('socialaggregator', '0002_auto_20160317_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='slug')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('short_description', models.TextField(verbose_name='short description', blank=True)),
                ('media_url', models.URLField(max_length=500, verbose_name='media url', blank=True)),
                ('media_url_type', models.CharField(blank=True, max_length=100, verbose_name='media url type', choices=[(b'url', b'url'), (b'image', b'image'), (b'video', b'video')])),
                ('priority', models.IntegerField(default=100, verbose_name='display priority')),
                ('activate', models.BooleanField(default=False, verbose_name='activate')),
                ('author', models.CharField(max_length=250, verbose_name='author')),
                ('language', models.CharField(max_length=2, verbose_name='language', blank=True)),
                ('resource_date', models.DateTimeField(verbose_name='resource date')),
                ('social_id', models.CharField(max_length=250, verbose_name='social_id', blank=True)),
                ('social_type', models.CharField(default=b'article', max_length=250, verbose_name='social plugin', choices=[(b'article', b'Article'), (b'youtube_search', b'Youtube Search'), (b'wordpress_rss', b'Wordpress RSS'), (b'twitter', b'Twitter'), (b'instagram', b'Instagram'), (b'facebook_fanpage', b'Facebook Fanpage')])),
                ('query', models.CharField(max_length=250, verbose_name='query', blank=True)),
                ('favorite', models.BooleanField(default=False, verbose_name='favorite')),
                ('view_size', models.CharField(default=b'default', max_length=100, verbose_name='view size', choices=[(b'default', b'default'), (b'xsmall', b'xsmall'), (b'small', b'small'), (b'medium', b'medium'), (b'large', b'large'), (b'xlarge', b'xlarge')])),
                ('text_display', models.CharField(default=b'default', max_length=100, verbose_name='text display', choices=[(b'default', b'default'), (b'bottom', b'bottom'), (b'top', b'top')])),
                ('button_label', models.CharField(max_length=100, verbose_name='button label', blank=True)),
                ('button_color', models.CharField(default=b'black', max_length=100, verbose_name='button color', choices=[(b'white', b'white'), (b'black', b'black'), (b'primary', b'primary'), (b'secondary', b'secondary'), (b'tertiary', b'tertiary')])),
                ('background_color', models.CharField(max_length=250, verbose_name='background color', blank=True)),
                ('new_page', models.BooleanField(default=False, verbose_name='open in new page')),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2016, 3, 17, 12, 32, 32, 324319), editable=False)),
                ('update_date', models.DateTimeField(default=None, editable=False)),
                ('updated', models.BooleanField(default=False, editable=False)),
                ('feeds', models.ManyToManyField(to='socialaggregator.Feed', verbose_name='feeds')),
                ('image', filer.fields.image.FilerImageField(default=None, validators=[socialaggregator.models.validate_image_size], to='filer.Image', blank=True, null=True, verbose_name='image')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
                ('thumbnail', filer.fields.image.FilerImageField(related_name='+', default=None, blank=True, to='filer.Image', null=True, verbose_name='thumbnail')),
            ],
            options={
                'ordering': ['updated', '-resource_date', 'query'],
                'verbose_name': 'resource',
                'verbose_name_plural': 'resources',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='ressource',
            name='feeds',
        ),
        migrations.RemoveField(
            model_name='ressource',
            name='image',
        ),
        migrations.RemoveField(
            model_name='ressource',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='ressource',
            name='thumbnail',
        ),
        migrations.DeleteModel(
            name='Ressource',
        ),
        migrations.AlterField(
            model_name='aggregator',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aggregator',
            name='social_plugin',
            field=models.CharField(max_length=250, verbose_name='social plugin', choices=[(b'youtube_search', b'Youtube Search'), (b'wordpress_rss', b'Wordpress RSS'), (b'twitter', b'Twitter'), (b'instagram', b'Instagram'), (b'facebook_fanpage', b'Facebook Fanpage')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feed',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
