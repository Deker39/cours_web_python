from django.shortcuts import render, HttpResponse

# global menu
menu = ['mobile app', 'book review']


def show(request):
    context = {
        'title': 'show',
        'menu': menu,
    }
    return render(request, 'show.html', context=context)
