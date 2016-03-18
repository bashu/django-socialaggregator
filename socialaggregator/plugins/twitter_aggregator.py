# -*- coding: utf-8 -*-

from datetime import datetime

from twitter import Twitter, OAuth

from socialaggregator.conf import settings

from .base import BaseAggregator


class Aggregator(GenericAggregator):

    CONSUMER_KEY = settings.SA_TWITTER_CONSUMER_KEY
    CONSUMER_SECRET = settings.SA_TWITTER_CONSUMER_SECRET
    TOKEN = settings.SA_TWITTER_TOKEN
    SECRET = settings.SA_TWITTER_SECRET

    datetime_format = "%a %b %d %H:%M:%S +0000 %Y"

    def init_connector(self):
        auth = OAuth(
            self.TOKEN, self.SECRET, self.CONSUMER_KEY, self.CONSUMER_SECRET)
        self.connector = Twitter(auth=auth)

    def search(self, query):
        res = self.connector.search.tweets(q=query)
        data = []
        for t in res['statuses']:
            item = {
                'social_id': t['id_str'],
                'name': 'tweet %s' % t['id_str'],
                'slug': 'tweet_%s' % t['id_str'],
                'language': t['lang'],
                'resource_date': datetime.strptime(
                    t['created_at'], self.datetime_format),
                'description': t['text'],
                'author': t['user']['name'],
            }
            data.append(item)
        return data
