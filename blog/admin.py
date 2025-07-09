from django.contrib import admin
from .models import Blog, SocialMediaIcon, BlogSocialMediaLink

admin.site.register(Blog)
admin.site.register(SocialMediaIcon)
admin.site.register(BlogSocialMediaLink)
