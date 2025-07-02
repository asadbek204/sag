from django.db import models
from core.base import BaseModel
from django.utils.translation import gettext_lazy as _


class CallCenter(BaseModel):
    phone_number = models.CharField(max_length=13, verbose_name = _('phone_number'))

    def __str__(self):
        return f'{self.phone_number}'

    class Meta:
        verbose_name = _('Call Center')
        verbose_name_plural = _('Call Center')


class SocialMedia(BaseModel):
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name = _('name'))
    image = models.ImageField(upload_to='social_media/', blank=True, verbose_name = _('image'))
    url = models.URLField(verbose_name = _('url'), blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Social Media')
        verbose_name_plural = _('Social Media')

