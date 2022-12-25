from django.http import *
from django.shortcuts import *
from .models import *


# Create your views here.
menu = ['about page','add state','feed back','Sing in']

def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Main Page'})

def about(request):
    return  render(request, 'women/about.html', {'menu': menu, 'title': 'About Main Page'})


def categories(request,catid):
    print(request.GET) if request.GET else False
    # print(request.POST) if request.POST else False

    return  HttpResponse(f'<h1>States categori</h1><p>{catid}</p>')

def archive(request,year):
    # if int(year) > 2022:
    #     raise Http404()
    if int(year) > 2022:
        return redirect('home',permanent=True)
    return  HttpResponse(f'<h1>Archive on year {year}</h1>')

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Sorry page not found</h1>')
