from modeltranslation.translator import register, TranslationOptions

from . models import *


@register(Related_links)
class Related_linksTranslate(TranslationOptions):
    fields = ('title', 'area', 'description')  # These are the fields you want to translate. 
