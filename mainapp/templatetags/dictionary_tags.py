from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def create_link(full_name):
    return full_name.replace(' ','+')
