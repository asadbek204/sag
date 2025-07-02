from django.contrib import admin
from .models import (
    Shape,
    CarpetModel,
    Carpet,
    Price,
    Color,
    Size,
    Room,
    Style,
    Catalog,
    CarpetModelImages,
)

admin.site.register(Shape)
admin.site.register(CarpetModel)
admin.site.register(Carpet)
admin.site.register(Price)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Room)
admin.site.register(Style)
admin.site.register(Catalog)
admin.site.register(CarpetModelImages)
