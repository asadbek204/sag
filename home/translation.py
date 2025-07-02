from modeltranslation.translator import translator, TranslationOptions
from .models import (
    Questions,
)


class QuestionsTranslationOptions(TranslationOptions):
    fields = ['question', 'answer']


translator.register(Questions, QuestionsTranslationOptions)
