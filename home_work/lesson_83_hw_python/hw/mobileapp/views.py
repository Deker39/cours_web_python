from django.shortcuts import render, HttpResponse, redirect
from .models import *

# global menu
menu = ['home', 'mobile', 'book']
pod_menu = ['add mobile', 'show mobile']


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
        'menu': menu,
        'pod_menu': pod_menu,
    }
    return render(request, 'form_add_mobile.html', context=context)


def successful(request):
    users = ValueMobileAppReview.objects.latest('id')
    context = {
        'title': 'successful',
        'menu': menu,
        'pod_menu': pod_menu,
        'users': users
    }

    return render(request, 'successful_mobile.html', context=context)


def show(request):
    users = ValueMobileAppReview.objects.all()
    context = {
        'title': 'show',
        'menu': menu,
        'pod_menu': pod_menu,
        'users': users
    }
    return render(request, 'show_mobile.html', context=context)


def index_mobile(request):
    context = {
        'title': 'mobile',
        'menu': menu,
        'pod_menu': pod_menu,
        'description': 'Mobile Page'
    }
    return render(request, 'index.html', context=context)


def index(request):
    context = {
        'title': 'index',
        'menu': menu,
        'description': 'Main Page'
    }
    return render(request, 'index.html', context=context)



