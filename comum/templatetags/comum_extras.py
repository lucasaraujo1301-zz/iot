import re
from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='add_css_class')
def add_css_class(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter(name='add_css_class_placeholder')
def add_css_class_placeholder(value, arg):
    arg = arg.split(',')

    return value.as_widget(attrs={'class': arg[0], 'placeholder': arg[1]})


@register.filter(name='remove_underline')
def remove_underline(value):
    return value.replace('_', ' ')


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)

    if hasattr(user, "groups"):
        return group in user.groups.all()
    else:
        return False


@register.filter(name='todos_fluxos')
def todos_fluxos(fluxos, status):
    status_fluxos = set(fluxos.values_list("status", flat=True))
    return (len(status_fluxos) == 1 and status in status_fluxos)


@register.filter(name='meu_fluxo')
def meu_fluxo(fluxos, user):
    meus_fluxos = fluxos.filter(responsavel=user).last()
    return (meus_fluxos.status)
