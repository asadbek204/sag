from django.db import models
from core.base import BaseModel
from django.utils.translation import gettext_lazy as _


class Blog(BaseModel):
    title = models.CharField(max_length=30, blank=True, null=True, verbose_name = _('title'))
    content = models.FileField(upload_to='blog/', verbose_name = _('content'))
    view_count = models.IntegerField(default=0, verbose_name = _('view_count'))
    telegram_link = models.URLField(verbose_name = _('telegram_link'))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blog')

