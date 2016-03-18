# -*- coding: utf-8 -*-

from datetime import datetime

from django.contrib import admin
from django.db import transaction
from django.db import IntegrityError
from django.utils.translation import ugettext_lazy as _

from .models import Feed, Aggregator, Resource


class FeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'date_created')
    search_fields = ('name', 'slug')
    list_filter = ('date_created',)
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'date_created'

admin.site.register(Feed, FeedAdmin)


class AggregatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'query', 'social_plugin', 'date_created')
    search_fields = ('name', 'slug', 'query',)
    list_filter = ('social_plugin', 'date_created')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'date_created'

admin.site.register(Aggregator, AggregatorAdmin)


class ResourceAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'author', 'priority', 'view_size', 'language',
        'social_type', 'query', 'resource_date', 'activate','updated',
    )
    search_fields = ('name', 'author', 'description', 'short_description')
    list_filter = ('social_type', 'feeds', 'view_size', 'language', 'activate', 'updated')
    list_editable = ('priority','view_size','activate',)
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'resource_date'

    actions = ['activate', 'deactivate', 'duplicate']

    fieldsets = (
        (None, {
            'fields': (
                'name', 'slug', 'description', 'short_description',
                'image', 'thumbnail', 'media_url', 'media_url_type','new_page',
            ),
        }),
        (_("Extra infos"), {
            'fields': (
                'priority', 'activate', 'author', 'language', 'feeds', 'resource_date', 'tags',
            ),
        }),
        (_("Social network infos"), {
            'fields': (
                'social_id', 'social_type', 'query',
            ),
        }),
        (_("Display infos"), {
            'fields': (
                'favorite', 'view_size', 'text_display', 'button_label', 'button_color', 'background_color',
            ),
        }),
    )

    def activate(self, request, queryset):
        with transaction.commit_on_success():
            queryset.update(activate=True)
    activate.short_description = _("Activate selected resources")

    def deactivate(self, request, queryset):
        with transaction.commit_on_success():
            queryset.update(activate=False)
    deactivate.short_description = _("Deactivate selected resources")

    def duplicate(self, request, queryset):
        with transaction.commit_on_success():
            for item in queryset:
                item.pk = None
                item.activate = False
                item.date_created = datetime.now()

                slug, name = item.slug + '_copy_%i', item.name + ' Copy %i'

                loop = 0
                while True:
                    try:
                        item.slug, item.name = slug % loop, name % loop
                        item.update_date = None
                        item.save()
                        break
                    except IntegrityError, e:
                        loop += 1
    duplicate.short_description = _("Duplicate selected resources")

admin.site.register(Resource, ResourceAdmin)
