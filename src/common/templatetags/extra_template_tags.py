from django import template

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
