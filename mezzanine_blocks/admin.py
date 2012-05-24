from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from mezzanine.conf import settings
from models import Block, RichBlock

class BlockAdmin(admin.ModelAdmin):
    ordering = ['title', ]
    list_display = ('title', 'login_required', 'show_title')
    search_fields = ('title', 'content')

    fieldsets = (
        (None, {
            "fields": ["title", "content", ],
        }),
        (_("Advanced data"), {
            "fields": ['login_required', 'show_title', "slug" ],
            "classes": ("collapse-closed",)
        }),
    )

    def in_menu(self):
        """
        Hide from the admin menu unless explicitly set in ``ADMIN_MENU_ORDER``.
        """
        for (name, items) in settings.ADMIN_MENU_ORDER:
            if "mezzanine_blocks.Block" in items:
                return True
        return False

class RichBlockAdmin(admin.ModelAdmin):
    ordering = ['title', ]
    list_display = ('title', 'login_required', 'show_title')
    search_fields = ('title', 'content')

    fieldsets = (
        (None, {
            "fields": ["title", "content", ],
        }),
        (_("Advanced data"), {
            "fields": ['login_required', 'show_title', "slug" ],
            "classes": ("collapse-closed",)
        }),
    )

    def in_menu(self):
        """
        Hide from the admin menu unless explicitly set in ``ADMIN_MENU_ORDER``.
        """
        for (name, items) in settings.ADMIN_MENU_ORDER:
            if "mezzanine_blocks.RichBlock" in items:
                return True
        return False

admin.site.register(Block, BlockAdmin)
admin.site.register(RichBlock, RichBlockAdmin)
