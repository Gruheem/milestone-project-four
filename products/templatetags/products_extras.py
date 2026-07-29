from django import template

register = template.Library()

# Performs the dictionary look up for the filter
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, [])