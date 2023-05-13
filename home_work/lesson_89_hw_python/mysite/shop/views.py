from django.shortcuts import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")