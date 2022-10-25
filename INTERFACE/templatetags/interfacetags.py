from django import template

register = template.Library()

@register.filter
def to_class_name(value):
    string = value.__class__.__name__
    result = ""
    for i in string:
        if i.isupper():
            result=result+" "+i.upper()
        else:
            result=result+i
    return result[1:]