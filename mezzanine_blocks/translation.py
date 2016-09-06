from modeltranslation.translator import register, TranslationOptions
from mezzanine_blocks.models import Block, RichBlock, ImageBlock


@register(Block)
class TranslatedBlock(TranslationOptions):
    fields = ('content',)


@register(RichBlock)
class TranslatedRichBlock(TranslationOptions):
    fields = ('title', 'content')


@register(ImageBlock)
class TranslatedImageBlock(TranslationOptions):
    fields = ('description', 'url')