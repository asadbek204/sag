from django.db import models
from core.base import BaseModel
from django.utils.translation import gettext_lazy as _


class AboutCompany(BaseModel):
    image = models.ImageField(upload_to='about/', blank=True, null=True, verbose_name=_("image"))
    title = models.CharField(max_length=300, blank=True, null=True, verbose_name=_("title"))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('About Company')
        verbose_name_plural = _('About Company')


class BriefAbout(BaseModel):
    title = models.CharField(max_length=250, blank=True, null=True, verbose_name=_("title"))
    description = models.TextField(blank=True, null=True, verbose_name=_("description"))
    image = models.ImageField(upload_to='about/', blank=True, null=True, verbose_name=_("image"))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('Brief About')
        verbose_name_plural = _('Brief About')


class ProductionVolume(BaseModel):
    year = models.PositiveIntegerField(default=0, verbose_name=_("year"))
    volume = models.CharField(max_length=300, verbose_name=_("volume"))

    def __str__(self):
        return f'{self.year}'

    class Meta:
        verbose_name = _('Production Volume')
        verbose_name_plural = _('Production Volume')


class AboutProduction(BaseModel):
    title = models.CharField(max_length=250, blank=True, null=True, verbose_name=_("title"))
    description = models.TextField(blank=True, null=True, verbose_name=_("description"))
    image = models.ImageField(upload_to='about/', blank=True, null=True, verbose_name=_("image"))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('About Production')
        verbose_name_plural = _('About Production')


class Gallery(BaseModel):
    image = models.ImageField(upload_to='about/', blank=True, null=True, verbose_name=_("image"))

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Gallery')

