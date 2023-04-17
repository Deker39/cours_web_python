from django.shortcuts import render, redirect
from .models import *

menu = ['home', 'mobile', 'book']
pod_menu = ['add book', 'show book']


def form_add(request):
    if request.method == 'POST':
        book = ValueBookReview()
        book.nick = request.POST.get('nick')
        book.rating = request.POST.get('rating')
        book.review = request.POST.get('review')
        book.spoiler = bool(request.POST.get('spoiler'))
        book.save()
        return redirect('./successful')

    context = {
        'title': 'add review',
        'menu': menu,
        'pod_menu': pod_menu,
    }
    return render(request, 'form_add_book.html', context=context)


def successful(request):
    reviews = ValueBookReview.objects.latest('id')
    context = {
        'title': 'show',
        'menu': menu,
        'pod_menu': pod_menu,
        'reviews': reviews
    }
    return render(request, 'successful_book.html', context=context)


def show(request):
    reviews = ValueBookReview.objects.all()
    context = {
        'title': 'show',
        'menu': menu,
        'pod_menu': pod_menu,
        'reviews': reviews
    }
    return render(request, 'show_book.html', context=context)


def index_book(request):
    context = {
        'title': 'book',
        'menu': menu,
        'pod_menu': pod_menu,
        'description': 'Book Page'
    }
    return render(request, 'index.html', context=context)
