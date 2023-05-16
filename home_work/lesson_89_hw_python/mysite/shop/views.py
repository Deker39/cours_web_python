from django.shortcuts import *


def index(request):
    context = {
        'title': 'main page'
    }
    return render(request, 'user_page.html', context=context)
