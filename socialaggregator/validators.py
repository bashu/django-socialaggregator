# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.template.defaultfilters import filesizeformat

from .conf import settings


@deconstructible
class ImageSizeValidator(object):
    size = settings.SA_RESOURCE_IMAGE_SIZE

    def __call__(self, value):
        if self.size != 0 and value.size > self.size * 1024:
            raise ValidationError(_("The image size (%s) is bigger than %s") % (
                filesizeformat(value.size), filesizeformat(self.size * 1024)))


