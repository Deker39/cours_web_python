from django.http import *
from django.shortcuts import *

from .forms import *
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
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                Women.objects.create(**form.cleaned_data)
                return  redirect('home')
            except:
                form.add_error(None,'post add error')
    else:
        form = AddPostForm()

    context = {
        'form': form,
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


def show_category(request, cat_slug):
    cat = Category.objects.filter(slug=cat_slug)
    posts = Women.objects.filter(cat_id=cat[0].id)

    print(posts)


    if len(posts) == 0:
        raise 404

    context = {
        'posts': posts,
        'title': 'Presentation by rubric',
        'cat_selected': cat[0].id,
    }

    return render(request, 'women/index.html', context=context)


def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Sorry page not found</h1>')


