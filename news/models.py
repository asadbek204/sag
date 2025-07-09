from django.db import models
from core.base import BaseModel
from blog.models import SocialMediaIcon
from django.utils.translation import gettext_lazy as _


class News(BaseModel):
    title = models.CharField(max_length=300, verbose_name = _('title'))
    description = models.TextField(verbose_name = _('description'))
    image = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name = _('image'))
    view_count = models.IntegerField(default=0, verbose_name=_('view_count'))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')


class NewsSocialMediaLink(BaseModel):
    news = models.ForeignKey(News, on_delete=models.CASCADE, blank=True, verbose_name=_('blog'))
    icon = models.ForeignKey(SocialMediaIcon, on_delete=models.CASCADE, blank=True, verbose_name=_('icon'))
    link = models.URLField(verbose_name=_('link'))

    def __str__(self):
        return f'{self.icon.name}'

    class Meta:
        verbose_name = _('News Social Media Link')
        verbose_name_plural = _('News Social Media Link')
