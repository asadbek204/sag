from django.contrib import admin
from .models import (
    AboutCompany,
    BriefAbout,
    ProductionVolume,
    Gallery,
    AboutProduction,
)

admin.site.register(AboutCompany)
admin.site.register(BriefAbout)
admin.site.register(ProductionVolume)
admin.site.register(Gallery)
admin.site.register(AboutProduction)
