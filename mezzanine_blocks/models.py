from django.db import models
from django.core.cache import cache
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.models import Slugged, RichText
from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.templatetags.mezzanine_tags import thumbnail
from mezzanine.utils.models import AdminThumbMixin
from .category import BlockCategory


class BaseBlock(Slugged):
    """Base Block
    """    
    category = models.ForeignKey(BlockCategory, null=True, blank=True)
    login_required = models.BooleanField(_("Login required"), help_text=_("If checked, only logged in users can view this page"), default=False)
    show_title     = models.BooleanField(_("Show title"), help_text=_("If checked, show block title"), default=False)


    def save(self, *args, **kwargs):
        super(BaseBlock, self).save(*args, **kwargs)
        cache.delete('%s%s' % ('mezzanine_blocks', self.slug))

    class Meta:
        abstract = True  

        
class Block(BaseBlock):
    """Content Block
    """        
    content = models.TextField(blank=True)

    class Meta:
        verbose_name = _('Block')
        verbose_name_plural = _('Blocks')


class RichBlock(BaseBlock, RichText):
    """RichText Block
    """       
    class Meta:
        verbose_name = _('Rich Block')
        verbose_name_plural = _('Rich Blocks')


class ImageBlock(BaseBlock, AdminThumbMixin):
    """An image Block
    """          
    image = FileField(verbose_name=_("Image"), upload_to="images", format="Image", max_length=255, null=True, blank=True)
    url = models.URLField(_("External URL"), max_length=255, blank=True, null=True, help_text=_("Optional URL."))
    description = RichTextField(_("Description"), blank=True, null=True)
    
    height = models.IntegerField(_("Height"), default=100, help_text=_("Height in pixels."))
    width = models.IntegerField(_("Width"), default=200, help_text=_("Width in pixels."))
    quality = models.IntegerField(_("Quality"), default=80)

    admin_thumb_field = "image"

    class Meta:
        verbose_name = _('Image Block')
        verbose_name_plural = _('Image Blocks')

    def get_url(self):
        return self.url or "#"

    def get_thumb_url(self):
        return thumbnail(thumb, self.width, self.height, self.quality)