# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from django_load.core import iterload
from django_load.core import load_object as l

from socialaggregator.models import Aggregator, Resource
from socialaggregator.conf import settings

AGGREGATORS = lambda: dict(
    (k, l(v['ENGINE'], "Aggregator")) for k, v in settings.SA_PLUGINS.items())


class Command(BaseCommand):
    help = 'Aggregate socials feeds'
    args = 'social_type1, [social_type2], social_type3'

    def handle(self, *args, **options):
        queryset = Aggregator.objects.all()
        if bool(args) is not None:
            queryset = queryset.filter(social_plugin__in=args)

        for obj in queryset:
            plugin = AGGREGATORS[obj.social_plugin]
            for data in plugin.search(obj.query):
                self.handle_resource(data, obj)

    def handle_resource(self, data, obj):
        if not Resource.objects.filter(social_id=data['social_id']).exists():
            r = Resource.objects.create(
                social_plugin=obj.social_plugin, query=obj.query, **data)

            for f in obj.feeds.all():
                r.feeds.add(f)
