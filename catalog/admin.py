from django.contrib import admin
from .models import (
    Shape,
    CarpetModel,
    Carpet,
    Price,
    Color,
    Size,
    Style,
    Catalog,
    CarpetModelImages,
    Character,
    CharacterDetail,
    CharacterTitle,
)

admin.site.register(Shape)
admin.site.register(CarpetModel)
admin.site.register(Carpet)
admin.site.register(Price)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Style)
admin.site.register(Catalog)
admin.site.register(CarpetModelImages)
admin.site.register(Character)
admin.site.register(CharacterDetail)
admin.site.register(CharacterTitle)
