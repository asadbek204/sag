from modeltranslation.translator import translator, TranslationOptions
from .models import (
    Catalog,
    Style,
    Room,
    Color,
    Shape,
)


class CatalogTranslationOptions(TranslationOptions):
    fields = ['name']


class StyleTranslationOptions(TranslationOptions):
    fields = ['name']


class RoomTranslationOptions(TranslationOptions):
    fields = ['name']


class ColorTranslationOptions(TranslationOptions):
    fields = ['name']


class ShapeTranslationOptions(TranslationOptions):
    fields = ['name']


translator.register(Catalog, CatalogTranslationOptions)
translator.register(Style, StyleTranslationOptions)
translator.register(Room, RoomTranslationOptions)
translator.register(Color, ColorTranslationOptions)
translator.register(Shape, ShapeTranslationOptions)