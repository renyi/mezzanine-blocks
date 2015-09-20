from modeltranslation.translator import translator, TranslationOptions
from mezzanine.core.translation import (TranslatedSlugged,
                                        TranslatedRichText)
from .models import Block, RichBlock


class TranslatedBlock(TranslatedSlugged):
    fields = ('content',)


class TranslatedRichBlock(TranslatedSlugged, TranslatedRichText):
    fields = ()


translator.register(Block, TranslatedBlock)
translator.register(RichBlock, TranslatedRichBlock)
