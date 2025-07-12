from django.db import models
from core.base import BaseModel
from django.utils.translation import gettext_lazy as _


class SocialMediaIcon(BaseModel):
    name = models.CharField(max_length=250, verbose_name = _('name'))
    image = models.ImageField(upload_to='social_media_icon/', blank=True, null=True, verbose_name = _('image'))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Social Media Icon')
        verbose_name_plural = _('Social Media Icon')


class Blog(BaseModel):
    title = models.CharField(max_length=250, blank=True, null=True, verbose_name = _('title'))
    description = models.TextField(verbose_name=_('description'))
    content = models.FileField(upload_to='blog/', verbose_name = _('content'))
    view_count = models.IntegerField(default=0, verbose_name = _('view_count'))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blog')


class BlogSocialMediaLink(BaseModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, verbose_name = _('blog'))
    icon = models.ForeignKey(SocialMediaIcon, on_delete=models.CASCADE, blank=True, verbose_name = _('icon'))
    link = models.URLField(verbose_name = _('link'))

    def __str__(self):
        return f'{self.icon.name}'

    class Meta:
        verbose_name = _('Blog Social Media Link')
        verbose_name_plural = _('Blog Social Media Link')




