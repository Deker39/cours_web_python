from django.shortcuts import *

# Create your views here.


def recipe(request):
    recipes = request.GET.get('recipe') if request.GET.get('recipe') else ''
    return HttpResponse(f'<h1>recipe: {recipes}</h1>')
