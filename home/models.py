from django.db import models
from core.base import BaseModel
from catalog.models import COLLECTION_TYPE
from django.utils.translation import gettext_lazy as _


class Header(BaseModel):
    image = models.ImageField(upload_to='header/', blank=True, verbose_name = _('image'))

    class Meta:
        verbose_name = _('Header')
        verbose_name_plural = _('Header')


class Questions(BaseModel):
    question = models.TextField(blank=True, null=True, verbose_name = _('question'))
    answer = models.TextField(blank=True, null=True, verbose_name = _('answer'))

    def __str__(self):
        return f'{self.question}'

    class Meta:
        verbose_name = _('Questions')
        verbose_name_plural = _('Questions')


class Collection(BaseModel):
    collection = models.IntegerField(choices=COLLECTION_TYPE, default=0, verbose_name = _('collection'))
    image = models.ImageField(upload_to='collection/', blank=True, null=True, verbose_name = _('image'))

    def __str__(self):
        return self.get_collection_display()

    class Meta:
        verbose_name = _('Collection')
        verbose_name_plural = _('Collection')





