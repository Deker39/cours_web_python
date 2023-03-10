from django import template
from women.models import *

register = template.Library()

# @register.simple_tag(name='getcats')
# def get_categories(filter=None):
#     return Category.objects.all() if not filter else Category.objects.filter(pk=filter)


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    cats = Category.objects.all() if not sort else Category.objects.order_by(sort)
    return  {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('women/list_menu.html')
def get_menu():
    menu = Menu.objects.all()
    return {'menu': menu}