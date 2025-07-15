from django.contrib import admin
from .models import Questions, Header, Collection, CarpetCollectionNews, CarpetDetailNews

admin.site.register(Questions)
admin.site.register(Header)
admin.site.register(Collection)
admin.site.register(CarpetCollectionNews)
admin.site.register(CarpetDetailNews)