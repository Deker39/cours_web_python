from django.http import *
from django.shortcuts import *
from .models import *


# Create your views here.
# 'about page', 'add state', 'feed back', 'Sing in'

def index(request):
    posts = Women.objects.all()

    context = {
        'posts': posts,
        'title': 'Main Page',
        'cat_selected': 0,
    }

    return render(request, 'women/index.html', context=context)


def about(request):
    context = {
        'title': 'About Main Page'
    }
    return  render(request, 'women/about.html', context=context)


def addpage(request):
    context = {
        'title': 'Add state'
    }
    return render(request, 'women/addpage.html', context=context)


def contact(request):
    context = {
        'title': 'Feedback'
    }
    return render(request, 'women/feedback.html', context=context)


def login(request):
    context = {
        'title': 'Login'
    }
    return render(request, 'women/login.html', context=context)

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return  render(request, 'women/post.html', context=context)


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise 404

    context = {
        'posts': posts,
        'title': 'Presentation by rubric',
        'cat_selected': cat_id,
    }

    return render(request, 'women/index.html', context=context)



def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Sorry page not found</h1>')


