import logging
from django import template
from django.template import loader
from django.db import models
from django.core.cache import cache
from mezzanine.conf import settings
from mezzanine.utils.urls import slugify
from mezzanine_blocks.models import Block, RichBlock, ImageBlock


register = template.Library()
logger = logging.getLogger(__name__)



class BasicFlatBlockWrapper(object):
    def prepare(self, parser, token):
        """
        The parser checks for following tag-configurations::

            {% flatblock {block} %}
            {% flatblock {block} {timeout} %}
            {% flatblock {block} using {tpl_name} %}
            {% flatblock {block} {timeout} using {tpl_name} %}
        """
        tokens = token.split_contents()
        self.is_variable = False
        self.tpl_is_variable = False
        self.slug = None
        self.cache_time = 0
        self.tpl_name = None
        tag_name, self.slug, args = tokens[0], tokens[1], tokens[2:]
        num_args = len(args)
        if num_args == 0:
            # Only the block name was specified
            pass
        elif num_args == 1:
            # block and timeout
            self.cache_time = args[0]
            pass
        elif num_args == 2:
            # block, "using", tpl_name
            self.tpl_name = args[1]
        elif num_args == 3:
            # block, timeout, "using", tpl_name
            self.cache_time = args[0]
            self.tpl_name = args[2]
        else:
            raise template.TemplateSyntaxError("%r tag should have between 1 and 4 arguments" % (tokens[0],))
        # Check to see if the slug is properly double/single quoted
        if not (self.slug[0] == self.slug[-1] and self.slug[0] in ('"', "'")):
            self.is_variable = True
        else:
            self.slug = self.slug[1:-1]
        # Clean up the template name
        if self.tpl_name is not None:
            if not(self.tpl_name[0] == self.tpl_name[-1] and self.tpl_name[0] in ('"', "'")):
                self.tpl_is_variable = True
            else:
                self.tpl_name = self.tpl_name[1:-1]
        if self.cache_time is not None and self.cache_time != 'None':
            self.cache_time = int(self.cache_time)

    def __call__(self, parser, token):
        self.prepare(parser, token)
        return FlatBlockNode(self.slug, self.is_variable, self.cache_time,
                template_name=self.tpl_name,
                tpl_is_variable=self.tpl_is_variable)

class RichFlatBlockWrapper(BasicFlatBlockWrapper):
    def __call__(self, parser, token):
        self.prepare(parser, token)
        return FlatBlockNode(self.slug, self.is_variable, self.cache_time,
                template_name=self.tpl_name,
                tpl_is_variable=self.tpl_is_variable, is_rich=True)

class ImageFlatBlockWrapper(BasicFlatBlockWrapper):
    def __call__(self, parser, token):
        self.prepare(parser, token)
        return FlatBlockNode(self.slug, self.is_variable, self.cache_time,
                template_name=self.tpl_name,
                tpl_is_variable=self.tpl_is_variable, is_image=True)

do_get_flatblock = BasicFlatBlockWrapper()
do_rich_flatblock = RichFlatBlockWrapper()
do_image_flatblock = ImageFlatBlockWrapper()

class FlatBlockNode(template.Node):
    def __init__(self, slug, is_variable, cache_time=0, with_template=True,
            template_name=None, tpl_is_variable=False, is_rich=False, is_image=False):

        if template_name is None:
            if is_image:
                self.template_name = 'mezzanine_blocks/image_block.html'
            else:
                self.template_name = 'mezzanine_blocks/block.html'
        else:
            if tpl_is_variable:
                self.template_name = template.Variable(template_name)
            else:
                self.template_name = template_name
        self.slug = slug
        self.is_variable = is_variable
        self.cache_time = cache_time
        self.with_template = with_template
        self.is_rich = is_rich
        self.is_image = is_image

    def render(self, context):
        if self.is_variable:
            real_slug = template.Variable(self.slug).resolve(context)
        else:
            real_slug = self.slug
        if isinstance(self.template_name, template.Variable):
            real_template = self.template_name.resolve(context)
        else:
            real_template = self.template_name

        real_title = real_slug
        real_slug = slugify(real_slug)

        # Eventually we want to pass the whole context to the template so that
        # users have the maximum of flexibility of what to do in there.
        if self.with_template:
            new_ctx = template.Context({})
            new_ctx.update(context)
        try:
            flatblock = None
            if self.cache_time != 0:
                cache_key = settings.MEZZANINE_BLOCKS_CACHE_PREFIX + real_slug
                flatblock = cache.get(cache_key)

            if flatblock is None:
                if self.is_rich:
                    _klass = RichBlock

                elif self.is_image:
                    _klass = ImageBlock

                else:
                    _klass = Block

                flatblock, created = _klass.objects.get_or_create(
                                  slug=real_slug,
                                  defaults = {'title': real_title}
                               )

                if self.cache_time != 0:
                    if self.cache_time is None or self.cache_time == 'None':
                        logger.debug("Caching %s for the cache's default timeout"
                                % (real_slug,))
                        cache.set(cache_key, flatblock)
                    else:
                        logger.debug("Caching %s for %s seconds" % (real_slug,
                            str(self.cache_time)))
                        cache.set(cache_key, flatblock, int(self.cache_time))
                else:
                    logger.debug("Don't cache %s" % (real_slug,))

            if self.with_template:
                tmpl = loader.get_template(real_template)
                new_ctx.update({'flatblock':flatblock})
                return tmpl.render(new_ctx)
            else:
                return flatblock.content
        except Block.DoesNotExist:
            return ''

register.tag('flatblock', do_get_flatblock)
register.tag('richflatblock', do_rich_flatblock)
register.tag('imageflatblock', do_image_flatblock)
