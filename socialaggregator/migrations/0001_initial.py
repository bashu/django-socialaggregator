# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import filebrowser.fields
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aggregator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('query', models.CharField(max_length=250, verbose_name='query')),
                ('social_plugin', models.CharField(max_length=250, verbose_name='social plugin', choices=[(b'edsa_wordpress_rss', b'Wordpress RSS'), (b'edsa_facebook_fanpage', b'Facebook Fanpage'), (b'edsa_youtube_search', b'Youtube search'), (b'edsa_instagram', b'Instagram'), (b'edsa_twitter', b'Twitter')])),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'aggregator',
                'verbose_name_plural': 'aggregators',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'feed',
                'verbose_name_plural': 'feeds',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ressource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='slug')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('short_description', models.TextField(verbose_name='short description', blank=True)),
                ('image', filebrowser.fields.FileBrowseField(default=None, max_length=255, null=True, verbose_name='image', blank=True)),
                ('thumbnail', filebrowser.fields.FileBrowseField(default=None, max_length=255, null=True, verbose_name='thumbnail', blank=True)),
                ('media_url', models.URLField(max_length=500, verbose_name='media url', blank=True)),
                ('media_url_type', models.CharField(blank=True, max_length=100, verbose_name='media url type', choices=[(b'url', b'url'), (b'image', b'image'), (b'video', b'video')])),
                ('priority', models.IntegerField(default=100, verbose_name='display priority')),
                ('activate', models.BooleanField(default=False, verbose_name='activate')),
                ('author', models.CharField(max_length=250, verbose_name='author')),
                ('language', models.CharField(max_length=2, verbose_name='language', blank=True)),
                ('ressource_date', models.DateTimeField(verbose_name='ressource date')),
                ('social_id', models.CharField(max_length=250, verbose_name='social_id', blank=True)),
                ('social_type', models.CharField(default=b'edsa_article', max_length=250, verbose_name='social plugin', choices=[(b'edsa_article', b'Article'), (b'edsa_wordpress_rss', b'Wordpress RSS'), (b'edsa_facebook_fanpage', b'Facebook Fanpage'), (b'edsa_youtube_search', b'Youtube search'), (b'edsa_instagram', b'Instagram'), (b'edsa_twitter', b'Twitter')])),
                ('query', models.CharField(max_length=250, verbose_name='query', blank=True)),
                ('favorite', models.BooleanField(default=False, verbose_name='favorite')),
                ('view_size', models.CharField(default=b'default', max_length=100, verbose_name='view size', choices=[(b'default', b'default'), (b'xsmall', b'Xsmall'), (b'small', b'small'), (b'medium', b'medium'), (b'large', b'large'), (b'xlarge', b'Xlarge')])),
                ('text_display', models.CharField(default=b'default', max_length=100, verbose_name='text display', choices=[(b'default', b'default'), (b'bottom', b'bottom'), (b'top', b'top')])),
                ('button_label', models.CharField(max_length=100, verbose_name='button label', blank=True)),
                ('button_color', models.CharField(default=b'black', max_length=100, verbose_name='button color', choices=[(b'white', b'white'), (b'black', b'black'), (b'primary', b'primary'), (b'secondary', b'secondary'), (b'tertiary', b'tertiary')])),
                ('background_color', models.CharField(max_length=250, verbose_name='background color', blank=True)),
                ('new_page', models.BooleanField(default=False, verbose_name='open in new page')),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2016, 3, 17, 10, 42, 2, 613436), verbose_name='creation date', editable=False)),
                ('update_date', models.DateTimeField(default=None, verbose_name='update date')),
                ('updated', models.BooleanField(default=False, verbose_name='updated')),
                ('feeds', models.ManyToManyField(to='socialaggregator.Feed', verbose_name='feeds')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'ordering': ('-priority', 'name'),
                'verbose_name': 'ressource',
                'verbose_name_plural': 'ressources',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='aggregator',
            name='feeds',
            field=models.ManyToManyField(to='socialaggregator.Feed', verbose_name='feeds'),
            preserve_default=True,
        ),
    ]
