from modeltranslation.translator import translator, TranslationOptions
from .models import (
    Catalog,
    Style,
    Color,
    Shape,
    Character,
    CharacterDetail,
)


class CatalogTranslationOptions(TranslationOptions):
    fields = ['name']


class StyleTranslationOptions(TranslationOptions):
    fields = ['name']


class ColorTranslationOptions(TranslationOptions):
    fields = ['name']


class ShapeTranslationOptions(TranslationOptions):
    fields = ['name']


class CharacterTranslationOptions(TranslationOptions):
    fields = ['name']


class CharacterDetailTranslationOptions(TranslationOptions):
    fields = ['detail', 'title']


translator.register(Catalog, CatalogTranslationOptions)
translator.register(Style, StyleTranslationOptions)
translator.register(Color, ColorTranslationOptions)
translator.register(Shape, ShapeTranslationOptions)
translator.register(Character, CharacterTranslationOptions)
translator.register(CharacterDetail, CharacterDetailTranslationOptions)