# -*- coding: utf-8 -*-

from django.conf import settings  # pylint: disable=W0611
from appconf import AppConf

gettext = lambda s: s


class SocialAggregatorSettings(AppConf):

    TWITTER_TOKEN = None
    TWITTER_SECRET = None
    TWITTER_CONSUMER_KEY = None
    TWITTER_CONSUMER_SECRET = None

    INSTAGRAM_ACCESS_TOKEN = None

    FACEBOOK_APP_ID = None
    FACEBOOK_APP_SECRET = None

    GOOGLE_DEVELOPER_KEY = None

    PAGINATED_BY = 16

    # Enabled plugins and their engine
    PLUGINS = {
        "twitter": {
            "ENGINE": "socialaggregator.plugins.twitter_noretweet_aggregator",
            "NAME": "Twitter"
        },
        "instagram": {
            "ENGINE": "socialaggregator.plugins.instagram_aggregator",
            "NAME": "Instagram"
        },
        "facebook_fanpage": {
            "ENGINE": "socialaggregator.plugins.facebook_fanpage_aggregator",
            "NAME": "Facebook Fanpage"
        },
        "wordpress_rss": {
            "ENGINE": "socialaggregator.plugins.wordpress_rss_aggregator",
            "NAME": "Wordpress RSS"
        },
        "youtube_search": {
            "ENGINE": "socialaggregator.plugins.youtube_search_aggregator",
            "NAME": "Youtube Search"
        },
    }

    # # Used templates
    # EDSA_VIEW_TEMPLATE = 'socialaggregator/ressource_list.html'
    # EDSA_TAG_TEMPLATE = 'socialaggregator/ressource_list_tag.html'
    # EDSA_PLUGIN_TEMPLATE = 'socialaggregator/cms_plugin_feed.html'

    # Image size limit (in Ko, use 0 for no size limit)
    RESOURCE_IMAGE_SIZE = 0

    # Various ressource fields choices
    RESOURCE_VIEW_SIZES = (
        ('default', gettext('default')),
        ('xsmall', gettext('xsmall')),
        ('small', gettext('small')),
        ('medium', gettext('medium')),
        ('large', gettext('large')),
        ('xlarge', gettext('xlarge')),
    )

    RESOURCE_TEXT_DISPLAY = (
        ('default', gettext('default')),
        ('bottom', gettext('bottom')),
        ('top', gettext('top')),
    )

    RESOURCE_BUTTON_COLORS = (
        ('white', gettext('white')),
        ('black', gettext('black')),
        ('primary', gettext('primary')),
        ('secondary', gettext('secondary')),
        ('tertiary', gettext('tertiary')),
    )

    RESOURCE_MEDIA_TYPES = (
        ('link', gettext('link')),
        ('image', gettext('image')),
        ('video', gettext('video')),
    )

    # Base media types to add to the ones from PLUGINS
    RESOURCE_BASE_MEDIA_TYPES = [
        ('article', 'Article'),
    ]

    class Meta:
        prefix = 'sa'
        holder = 'socialaggregator.conf.settings'
