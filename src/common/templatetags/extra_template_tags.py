# -*- coding: utf-8 -*-
from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def js(js_file_path, prefix='/static/js/'):
    """
    path is a relative path starting from static/js/ folder
    :param path:
    :return:
    """
    relative_path = prefix + js_file_path
    return '<script src="{}" type="text/javascript"></script>'.format(relative_path)


@register.simple_tag
def css(css_file_path, prefix='/static/css/'):
    """
    path is a relative path starting from static/css/ folder
    :param path:
    :return:
    """
    relative_path = prefix + css_file_path
    return '<link href="{}"  type="text/css" rel="stylesheet" />'.format(relative_path)


@register.filter
def to_str(value):
    return unicode(value)

@register.simple_tag
def image_link(value):
    prefix = settings.MEDIA_URL
    return prefix + value if not value.startswith('/static') else value