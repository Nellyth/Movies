from django import template
register = template.Library()


@register.filter
def data(value):
    return value.all()


@register.filter
def url(value):
    try:
        if '=' in value:
            value = value.split('=')
            return value[1]
        else:
            return value
    except Exception:
        return value