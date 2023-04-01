from django.shortcuts import *

# Create your views here.


def helloworld(request, lang='en'):
    if lang == 'en':
        return HttpResponse('<h1>Hello, World</h1>')
    elif lang == 'fr':
        return HttpResponse('<h1>Bonjour, le monde</h1>')
    elif lang == 'de':
        return HttpResponse('<h1>Hallo, Welt</h1>')
    elif lang == 'es':
        return HttpResponse('<h1>Hola, Mundo</h1>')
    else:
        return HttpResponse('<h1>Unknowns lang</h1>')


