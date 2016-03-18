# -*- coding: utf-8 -*-

from datetime import datetime

from django.db import models
from django.utils.importlib import import_module
from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _

from taggit.managers import TaggableManager
from filer.fields.image import FilerImageField
from django_extensions.db.fields import (
    CreationDateTimeField, ModificationDateTimeField)

from .managers import ResourceManager, ActivatedManager
from .conf import settings


def build_social_plugins_list():
    return [(plugin, data["NAME"]) for plugin, data in
            settings.SA_PLUGINS.items()]

def validate_image_size(value):
    size = settings.SA_RESOURCE_IMAGE_SIZE
    if size != 0 and value.size > size * 1024:
        raise ValidationError(_("The image size (%s) is bigger than %s") % (
            filesizeformat(value.size), filesizeformat(size * 1024)))

SOCIAL_PLUGINS = build_social_plugins_list()


class Feed(models.Model):

    name = models.CharField(_('name'), max_length=250)
    slug = models.SlugField(_('slug'), unique=True, max_length=100)

    # for internal use
    
    date_created = CreationDateTimeField(editable=False, db_index=True)

    class Meta:
        verbose_name = _('feed')
        verbose_name_plural = _('feeds')

    def __unicode__(self):
        return self.name


class Aggregator(models.Model):

    name = models.CharField(_('name'), max_length=250)
    slug = models.SlugField(_('slug'), unique=True, max_length=100)

    query = models.CharField(_('query'), max_length=250)

    social_plugin = models.CharField(_('social plugin'), max_length=250, choices=SOCIAL_PLUGINS)

    feeds = models.ManyToManyField(Feed, verbose_name=_('feeds'))

    # for internal use

    date_created = CreationDateTimeField(editable=False, db_index=True)

    class Meta:
        verbose_name = _('aggregator')
        verbose_name_plural = _('aggregators')

    def __unicode__(self):
        return self.name


class Resource(models.Model):

    name = models.CharField(_('name'), max_length=250)
    slug = models.SlugField(_('slug'), unique=True, max_length=100)

    description = models.TextField(_('description'), blank=True)
    short_description = models.TextField(_('short description'), blank=True)

    image = FilerImageField(
        verbose_name=_('image'), validators=[validate_image_size], null=True, blank=True, default=None)
    thumbnail = FilerImageField(
        verbose_name=_('thumbnail'), related_name="+", null=True, blank=True, default=None)

    media_url = models.URLField(_('media url'), blank=True, max_length=500)
    media_url_type = models.CharField(
        verbose_name=_('media url type'), max_length=100,
        choices=settings.SA_RESOURCE_MEDIA_TYPES,
        blank=True,
    )

    # extra infos
    priority = models.IntegerField(_('display priority'), default=100)
    activate = models.BooleanField(_('activate'), default=False)
    author = models.CharField(_('author'), max_length=250)
    language = models.CharField(_('language'), max_length=2, blank=True)
    feeds = models.ManyToManyField(Feed, verbose_name=_('feeds'))
    resource_date = models.DateTimeField(_('resource date'))

    # social network info
    social_id = models.CharField(_('social_id'), max_length=250, blank=True)
    social_type = models.CharField(
        verbose_name=_('social plugin'), max_length=250,
        choices=settings.SA_RESOURCE_BASE_MEDIA_TYPES + SOCIAL_PLUGINS,
        default='article',
    )
    query = models.CharField(_('query'), max_length=250, blank=True)

    # display infos
    favorite = models.BooleanField(_('favorite'), default=False)
    view_size = models.CharField(
        verbose_name=_('view size'), max_length=100,
        choices=settings.SA_RESOURCE_VIEW_SIZES, default='default',
        blank=False,
    )
    text_display = models.CharField(
        verbose_name=_('text display'), max_length=100,
        choices=settings.SA_RESOURCE_TEXT_DISPLAY, default='default',
        blank=False,
    )
    button_label = models.CharField(_('button label'), max_length=100, blank=True)
    button_color = models.CharField(
        verbose_name=_('button color'), max_length=100,
        choices=settings.SA_RESOURCE_BUTTON_COLORS, default='black',
        blank=False,
    )
    background_color = models.CharField(_('background color'), max_length=250, blank=True)
    new_page = models.BooleanField(_('open in new page'), default=False)

    # for internal use

    tags = TaggableManager(blank=True)

    creation_date = models.DateTimeField(default=datetime.now(), editable=False)
    update_date = models.DateTimeField(editable=False, default=None)
    updated = models.BooleanField(editable=False, default=False)

    objects = ResourceManager()
    activated = ActivatedManager()

    class Meta:
        verbose_name = _('resource')
        verbose_name_plural = _('resources')
        ordering = ['updated', '-resource_date', 'query']

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.update_date = datetime.now()
        if self.update_date and not self.updated:
            self.updated = True
        super(Resource, self).save(*args, **kwargs)

    # def get_unified_render(self):
    #     """
    #     Get the formatter for ressource datas then return the unified data render
    #     """
    #     formatter_path = getattr(
    #         settings, "SA_RESOURCE_FORMATTER", "socialaggregator.formatter.RessourceFormatterDefault",
    #     )
    #     dot = formatter_path.rindex('.')
    #     module_name = formatter_path[:dot]
    #     class_name = formatter_path[dot + 1:] # Assume last item is the class to load
    #     try:
    #         _class = getattr(import_module(module_name), class_name)
    #     except ImportError:
    #         raise ImportError("'%s' cannot be imported from the setting 'RESOURCE_FORMATTER'" % formatter_path)
    #     except AttributeError:
    #         raise AttributeError("'%s' cannot be imported from the setting 'RESOURCE_FORMATTER'" % formatter_path)
    #     else:
    #         return _class(self).render()

# # Optional plugin for DjangoCMS if installed
# try:
#     from cms.models import CMSPlugin
# except ImportError:
#     pass
# else:
#     class FeedPlugin(CMSPlugin):
#         feed = models.ForeignKey('socialaggregator.Feed', related_name='plugins')

#         def __unicode__(self):
#             return self.feed.name
