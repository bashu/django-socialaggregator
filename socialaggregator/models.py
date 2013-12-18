"""Models for parrot.gallery"""
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from taggit.managers import TaggableManager


def build_social_plugins_list():
    return [(plugin, datas["NAME"]) for plugin, datas in
             settings.EDSA_PLUGINS.items()]

SOCIAL_PLUGINS = build_social_plugins_list()


class Feed(models.Model):
    """Model for group ressource by feed"""

    name = models.CharField(_('name'), max_length=250)
    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)
    slug = models.SlugField(_('slug'), unique=True, max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('feed')
        verbose_name_plural = _('feeds')


class Aggregator(models.Model):
    """Model for an social feed aggregator"""

    name = models.CharField(_('name'), max_length=250)
    query = models.CharField(_('query'), max_length=250)
    social_plugin = models.CharField(_('social plugin'), max_length=250,
                                     choices=SOCIAL_PLUGINS)
    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)
    slug = models.SlugField(_('slug'), unique=True, max_length=100)
    feeds = models.ManyToManyField(Feed, verbose_name=_('feeds'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('aggregator')
        verbose_name_plural = _('aggregators')


class Ressource(models.Model):
    """Model representing a ressource"""

    VIEW_SIZES = (('default', _('default')),
                  ('xsmall', _('Xsmall')),
                  ('small', _('small')),
                  ('medium', _('medium')),
                  ('large', _('large')),
                  ('xlarge', _('Xlarge')),
                  )

    TEXT_DISPLAY = (('default', _('default')),
                    ('bottom', _('bottom')),
                    ('top', _('top')),
                    )

    SOCIAL_LIST = [('edsa_article', 'Article'),] + SOCIAL_PLUGINS

    social_id = models.CharField(_('social_id'), max_length=250, blank=True)
    name = models.CharField(_('name'), max_length=250)
    slug = models.SlugField(_('slug'), unique=True, max_length=100)
    description = models.TextField(_('description'), blank=True)
    short_description = models.TextField(_('short description'), blank=True)
    image = models.ImageField(_('image'), upload_to='social_aggregator',
                              blank=True)
    thumbnail = models.ImageField(_('thumbnail'),
                                  upload_to='social_aggregator/thumbs',
                                  blank=True)
    view_size = models.CharField(_('view size'), max_length=100,
                                 choices=VIEW_SIZES, blank=False,
                                 default='default')
    text_display = models.CharField(_('text display'), max_length=100,
                                    choices=TEXT_DISPLAY, blank=False,
                                    default='default')
    author = models.CharField(_('author'), max_length=250)
    language = models.CharField(_('language'), max_length=2)
    ressource_date = models.DateTimeField(_('ressource date'))
    feeds = models.ManyToManyField(Feed, verbose_name=_('feeds'))
    social_type = models.CharField(_('social plugin'), max_length=250,
                                   choices=SOCIAL_LIST,
                                   default="edsa_article")
    query = models.CharField(_('query'), max_length=250)
    tags = TaggableManager(blank=True)
    priority = models.IntegerField(_('display priority'), default=100)
    activate = models.BooleanField(_('activate'), default=False)
    favorite = models.BooleanField(_('favorite'), default=False)
    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)
    update_date = models.DateTimeField(_('update date'), auto_now=True)

    @models.permalink
    def get_absolute_url(self):
        return ('social_aggregator_ressource_detail', (self.slug,))

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('-priority', 'name')
        verbose_name = _('ressource')
        verbose_name_plural = _('ressources')
