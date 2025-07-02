from django.db import models
from core.base import BaseModel
from django.utils.translation import gettext_lazy as _


class AboutMethod(BaseModel):
    title = models.CharField(max_length=250, blank=True, null=True, verbose_name = _('title'))
    description = models.TextField(blank=True, null=True, verbose_name = _('description'))
    image = models.ImageField(upload_to='method/', blank=True, verbose_name = _('image'))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('About Method')
        verbose_name_plural = _('About Method')


class Content(BaseModel):
    title = models.CharField(max_length=300, blank=True, null=True, verbose_name = _('title'))
    description = models.TextField(blank=True, null=True, verbose_name = _('description'))
    image = models.ImageField(upload_to='method/', blank=True, null=True, verbose_name = _('image'))
    icon = models.ImageField(upload_to='method/', blank=True, null=True, verbose_name = _('icon'))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('Content')
        verbose_name_plural = _('Content')


class Material(BaseModel):
    image = models.ImageField(upload_to='method/', blank=True, null=True, verbose_name = _('image'))

    class Meta:
        verbose_name = _('Material')
        verbose_name_plural = _('Material')


class ProductGallery(BaseModel):
    image = models.ImageField(upload_to='method/', blank=True, null=True, verbose_name = _('image'))

    class Meta:
        verbose_name = _('Product Gallery')
        verbose_name_plural = _('Product Gallery')
