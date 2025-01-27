from django import template
from typing import Any

register = template.Library()

@register.filter
def dict_get(dictionary: dict, key: str) -> Any:
    try:
        return dictionary.get(key, "")
    except AttributeError:
        return ""

@register.filter
def replace(value: str, arg: str) -> str:
    old, new = arg.split(',')
    return value.replace(old, new)

@register.filter
def capitalize(value:str) -> str:
    return value.capitalize()