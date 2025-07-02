from modeltranslation.translator import translator, TranslationOptions
from .models import Blog


class BlogTranslationOptions(TranslationOptions):
    fields = ['title']


translator.register(Blog, BlogTranslationOptions)

