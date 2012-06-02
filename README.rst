Overview
========
A mezzanine flavored fork of django-flatblocks (https://github.com/zerok/django-flatblocks).
The goal of this project is to be able to easily create custom blocks of HTML
in the template, and can be editable via admin.

Installation
============
1. Add "mezzanine_blocks" to INSTALLED_APPS:

    INSTALLED_APPS = (
        "...",
        "mezzanine_blocks",
    )

2. Add "Blocks" menu item to admin menu (Optional):

    ADMIN_MENU_ORDER = (
        ("Content", (
                "pages.Page",
                "mezzanine_blocks.Block",
                "blog.BlogPost",
                "blog.BlogCategory",
                "generic.ThreadedComment",
                ("Media Library", "fb_browse"),
            )
        ),
    )

3. Run "python manage.py createdb" or "python manage.py syncdb && "python manage.py migrate".

Usage
=====
1. Include block_tags in the template:

    {% load ... block_tags %}

2. Insert block anywhere in the template:

    {% flatblock "My Awesome Block" %}

    {% richflatblock "My Awesome HTML Block" %}

3. You should see the blocks in the admin.

Options
=======
Options are similar to django-flatblocks.

    {% flatblock {block} %}
    {% flatblock {block} {timeout} %}
    {% flatblock {block} using {tpl_name} %}
    {% flatblock {block} {timeout} using {tpl_name} %}

    {% richflatblock {block} %}
    {% richflatblock {block} {timeout} %}
    {% richflatblock {block} using {tpl_name} %}
    {% richflatblock {block} {timeout} using {tpl_name} %}

Future Enhancements
===================
1. Include more mezzanine flavored goodies (front-end editing, multi site, etc. ).
