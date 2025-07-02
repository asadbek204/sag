from modeltranslation.translator import translator, TranslationOptions
from .models import AboutCompany, BriefAbout, AboutProduction


class AboutCompanyTranslationOptions(TranslationOptions):
    fields = ['title']


class BriefAboutTranslationOptions(TranslationOptions):
    fields = ['title', 'description']


class CategoryTranslationOptions(TranslationOptions):
    fields = ['title', 'description']


translator.register(AboutCompany, AboutCompanyTranslationOptions)
translator.register(BriefAbout, BriefAboutTranslationOptions)
translator.register(AboutProduction, CategoryTranslationOptions)

