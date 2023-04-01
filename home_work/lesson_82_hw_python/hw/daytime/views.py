import datetime

from django.shortcuts import *

# Create your views here.


def daytime(request):
    now = datetime.datetime.now()
    g = ''
    if 6 <= now.hour < 12:
        g = 'good morning'
    elif 12 <= now.hour < 18:
        g = 'good day'
    elif 18 <= now.hour <= 24:
        g = 'good evening'
    else:
        g = 'good night'

    return HttpResponse(f'<h1>{now.strftime("%d/%m/%Y %H:%M:%S")} :: {g}</h1>')
