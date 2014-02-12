from __future__ import unicode_literals
from django import template

register = template.Library()


def end_date(value):
    if value is None:
        return 'Current'
    else:
        return value.strftime('%b %Y')


register.filter('end_date', end_date)