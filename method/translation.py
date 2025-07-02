from modeltranslation.translator import translator, TranslationOptions
from .models import (
    Content,
    AboutMethod,
)


class ContentTranslationOptions(TranslationOptions):
    fields = ['title', 'description']


class AboutMethodTranslationOptions(TranslationOptions):
    fields = ['title', 'description']


translator.register(Content, ContentTranslationOptions)
translator.register(AboutMethod, AboutMethodTranslationOptions)