from django.contrib import admin
from .models import (
    Content,
    Material,
    ProductGallery,
    AboutMethod
)

admin.site.register(Content)
admin.site.register(Material)
admin.site.register(ProductGallery)
admin.site.register(AboutMethod)