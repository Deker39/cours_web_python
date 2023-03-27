from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponsePermanentRedirect, JsonResponse


class Person:
    def __init__(self, name: str, age: int, ids: list):
        self.name = name
        self.age = age
        self.customers_id = ids


# Create your views here.
def index(request: WSGIRequest):
    # data = {
    #     "name": request.user,
    #     "message": "message from back-end"
    # }
    person = Person("Alex", 20, [32, 12, 55])
    # ls = [32, 12, 55]
    # user = {"name": "Alex", "age":20}
    # addr = ("Street", 23,1)
    # data = {"user": user, "customers": ls, "address": addr,
    #         "message": "message from back-end"}
    return render(request, "index.html",
                  context={"person": person,
                           "data": "22.02.2002"})


def persons(requesr: WSGIRequest):
    person = {
        "name": "ALEX",
        "age": 50
    }
    return JsonResponse(person)


def home(request: WSGIRequest):
    return HttpResponse('<h1>Home</h1>')


def lviv(request: WSGIRequest):
    return HttpResponse('<h1>lviv</h1>')


def kiev(request: WSGIRequest):
    return HttpResponse('<h1>kiev</h1>')


def contact(request: WSGIRequest):
    return HttpResponse('<h1>contact</h1>')


def products(request: WSGIRequest, id):
    print(request)
    return HttpResponse(f'<h1>product id: {id}</h1>', content_type='text/plain',
                        charset="UTF-8", status=506, reason='Chototo')


def user_empty(request):
    return HttpResponseBadRequest("/")


def user(request: WSGIRequest, name: str, age: int):
    return HttpResponse(f'<h1>Name: {name}</h1><h1>Age: {age}</h1>')
