from django.shortcuts import render, HttpResponse, redirect
from .models import *

# global menu
global_menu = ['home', 'mobile', 'book']
name_menu = ['add', 'show']
url_menu = ['add mobile', 'show mobile']
list_menu = [[name, url] for name, url in zip(name_menu, url_menu)]


def form_add(request):
    if request.method == 'POST':
        user = ValueMobileAppReview()
        user.nick = request.POST.get('nick')
        user.email = request.POST.get('email')
        user.amount_star = request.POST.get('amount_star')
        user.describe = request.POST.get('describe')
        user.save()
        return redirect('./successful')

    context = {
        'title': 'add user',
        'menu': global_menu,
        'list_menu': list_menu,
    }
    return render(request, 'form_add_mobile.html', context=context)


def successful(request):
    users = ValueMobileAppReview.objects.latest('id')
    context = {
        'title': 'successful',
        'menu': global_menu,
        'list_menu': list_menu,
        'users': users
    }

    return render(request, 'successful_mobile.html', context=context)


def show(request):
    users = ValueMobileAppReview.objects.all()
    context = {
        'title': 'show',
        'menu': global_menu,
        'list_menu': list_menu,
        'users': users
    }
    return render(request, 'show_mobile.html', context=context)


def index_mobile(request):
    context = {
        'title': 'mobile',
        'menu': global_menu,
        'list_menu': list_menu,
        'description': 'Mobile Page'
    }
    return render(request, 'index.html', context=context)


def index(request):
    context = {
        'title': 'index',
        'menu': global_menu,
        'description': 'Main Page'
    }
    return render(request, 'index.html', context=context)



