from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.models import Slugged, RichText
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
