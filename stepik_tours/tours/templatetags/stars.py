from django import template


register = template.Library()


@register.filter()
def stars(value):
    stars = int(value)
    return '★' * stars
