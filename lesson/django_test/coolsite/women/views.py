from django.http import *
from django.shortcuts import *
from .models import *


# Create your views here.
# 'about page', 'add state', 'feed back', 'Sing in'
menu = [{'title': "About page", 'url_name': 'about'},
        {'title': "Add state", 'url_name': 'add_page'},
        {'title': "Feed back", 'url_name': 'contact'},
        {'title': "Sing in", 'url_name': 'login'}
        ]


def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Main Page'
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'About Main Page'
    }
    return  render(request, 'women/about.html', context=context)


def addpage(request):
    context = {
        'menu': menu,
        'title': 'Add state'
    }
    return render(request, 'women/addpage.html', context=context)


def contact(request):
    context = {
        'menu': menu,
        'title': 'Feedback'
    }
    return render(request, 'women/feedback.html', context=context)


def login(request):
    context = {
        'menu': menu,
        'title': 'Login'
    }
    return render(request, 'women/login.html', context=context)

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')



def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Sorry page not found</h1>')
