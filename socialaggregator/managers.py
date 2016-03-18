# -*- coding: utf-8 -*-

from datetime import datetime

from django.db import models
from django.db.models.query import QuerySet


class ResourceQuerySet(QuerySet):

    def update(self, *args, **kwargs):
        kwargs['update_date'] = datetime.now()
        kwargs['updated'] = True
        super(ResourceQuerySet, self).update(*args, **kwargs)


class ResourceManager(models.Manager):

    def get_queryset(self):
        return ResourceQuerySet(self.model, using=self._db)


class ActivatedManager(ResourceManager):

    def get_queryset(self):
        return super(ActivatedManager, self).get_queryset().filter(
            activate=True)
