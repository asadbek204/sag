from django.db import models
from core.base import BaseModel
from django.utils.translation import gettext_lazy as _


CHOICES_CITY = (
    (1, 'TASHKENT REGION'),
    (2, 'TASHKENT CITY'),
    (3, 'SIRDARYO REGION'),
    (4, 'JIZZAX REGION'),
    (5, 'SAMARKAND REGION'),
    (6, 'KASHKADARYA REGION'),
    (7, 'SURKHANDARYO REGION'),
    (8, "FERGANA REGION"),
    (9, 'BUKHARA REGION'),
    (10, 'NAMANGAN REGION'),
    (11, 'ANDIJAN REGION'),
    (12, 'NAVOI REGION'),
    (13, 'KHORAZIM REGION'),
    (14, 'REPUBLIC OF KARAKALPAKHSTAN'),
)


class Contact(BaseModel):
    full_name = models.CharField(max_length=300, verbose_name = _('full name'))
    phone_number = models.CharField(max_length=13, verbose_name = _('phone number'))
    city = models.IntegerField(choices=CHOICES_CITY, default=1, verbose_name = _('city'))
    address = models.TextField(blank=True, null=True, verbose_name = _('address'))
    comment = models.TextField(blank=True, null=True, verbose_name = _('comment'))

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contact')

