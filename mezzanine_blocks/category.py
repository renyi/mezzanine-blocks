from django.db import models
from django.core.cache import cache
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.models import Slugged


try:
    from mptt.models import MPTTModel, TreeForeignKey

    class BaseBlockCategory(MPTTModel, Slugged):
        """Base Category (MPTT tree).
        """
        parent = TreeForeignKey('self', null=True, blank=True, related_name='child')

        class Meta:
            abstract = True

        class MPTTMeta:
            order_insertion_by = ['title']

except ImportError:
    class BaseBlockCategory(Slugged):
        """Base Category
        """
        class Meta:
            abstract = True


class BlockCategory(BaseBlockCategory):
    """Block Category
    """
    class Meta:
        verbose_name = _('Block category')
        verbose_name_plural = _('Block categories')
