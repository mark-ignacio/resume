from __future__ import unicode_literals
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


def end_date(value):
    if value is None:
        return 'Current'
    else:
        return value.strftime('%b %Y')


@register.filter('markdown', is_safe=True)
@stringfilter
def markdown_shiv(value, safe=False):
    return mark_safe(markdown.markdown(force_unicode(value), safe_mode=safe, enable_attributes=True))


register.filter('end_date', end_date)