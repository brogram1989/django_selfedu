from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import  *

# Create your views here.
def main_page(request):
    return HttpResponse("Bismillahir rohmanir rohiym")

#
# def index(request): #HttpRequest
#     return HttpResponse("<h1>MW_INFO prilojeniyasi bosh sahifasi</h1>"+"\nMW_INFO prilojeniyasi")

def index(request):
    posts = MwInfo.objects.all()
    context = {
        'posts':posts,
        'title':'Bosh sahifa',
        'cat_selected': 0,
    }
    return render(request, 'mw_info/index.html', context = context)


def show_category(request, cat_id):
    posts = MwInfo.objects.filter(cat_id =cat_id)
    context = {
        'posts': posts,
        'title': 'bu Bo`lim bo`yicha ko`rsatish',
        'cat_selected': 0,
    }
    return render(request, 'mw_info/index.html', context=context)


def about(request):
    return render(request, "mw_info/about.html", {'title':"Sayt haqida"})

def addpage(request):
    return HttpResponse('sahifa qo`shish')

def contact(request):
    return HttpResponse('bog`lanish')

def login(request):
    return HttpResponse('kirish')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>voy, sahifa topilmadiku</h1>')

def show_post(request, post_id):
    return HttpResponse(f'id = {post_id } bo`lgan maqolani ko`rish ')


