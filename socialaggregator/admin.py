"""Admin for parrot.gallery"""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from socialaggregator.models import Feed
from socialaggregator.models import Aggregator
from socialaggregator.models import Ressource


class FeedAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Feed, FeedAdmin)


class AggregatorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Aggregator, AggregatorAdmin)


def make_activated(modeladmin, request, queryset):
    queryset.update(activate=True)
make_activated.short_description = _("Mark selected ressources as activated")


def make_unactivated(modeladmin, request, queryset):
    queryset.update(activate=False)
make_unactivated.short_description = _("Mark selected ressources as \
                                        unactivated")


class RessourceAdmin(admin.ModelAdmin):
    date_hierarchy = 'ressource_date'
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'author', 'language', 'social_type', 'query',
                    'ressource_date', 'activate', 'updated')
    list_filter = ('social_type', 'activate', 'updated', 'feeds', 'language')
    ordering = ['updated', '-ressource_date', 'query']
    exclude = ('updated', 'update_date',)
    actions = [make_activated, make_unactivated]

admin.site.register(Ressource, RessourceAdmin)
