from django.shortcuts import *

# Create your views here.


def sport(request, type_sport='main'):

    if type_sport == 'main':
        return HttpResponse(f'<h1>{type_sport}</h1>')
    elif type_sport == 'football':
        return HttpResponse(f'<h1>type sport: {type_sport}</h1>')
    elif type_sport == 'hockey':
        return HttpResponse(f'<h1>type sport: {type_sport}</h1>')
    elif type_sport == 'basketball':
        return HttpResponse(f'<h1>type sport: {type_sport}</h1>')
    else:
        return HttpResponse('<h1>Unknown type sport</h1>')
