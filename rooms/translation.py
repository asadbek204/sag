from modeltranslation.translator import translator, TranslationOptions
from .models import (
    Room,
    RoomImage,

)


class RoomTranslationOptions(TranslationOptions):
    fields = ['name']


class RoomImageTranslationOptions(TranslationOptions):
    fields = ['name']

translator.register(Room, RoomTranslationOptions)
translator.register(RoomImage, RoomImageTranslationOptions)