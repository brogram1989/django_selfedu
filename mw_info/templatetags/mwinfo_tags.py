from django import template
from mw_info.models import *


register = template.Library()

@register.simple_tag(name='get_categories')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('mw_info/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {'cats':cats, 'cat_selected':cat_selected}

@register.inclusion_tag('mw_info/list_categories.html')
def show_menu():
    menu = [{'title': 'Sayt haqida', 'url_name': 'about'},
            {'title': 'Maqola qo`shish', 'url_name': 'add_page'},
            {'title': 'bog`lanish', 'url_name': 'contact'},
            {'title': 'Kirish', 'url_name': 'login'},
            ]
    return {'menu':menu}




