import json

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponsePermanentRedirect, JsonResponse

from .models import User

# class Person:
#     def __init__(self, name: str, age: int, ids: list):
#         self.name = name
#         self.age = age
#         self.customers_id = ids


# class User:
#     id = 0
#     def __init__(self, name: str, phone: str):
#         self.id = User.id
#         self.name = name
#         self.phone = phone
#         User.id += 1
#
#     def __del__(self):
#         User.id -= 1


# ls = [User('Alex', '+790214012')]

# QuerySet.all
# User.objects.all().delete()
# result = User.objects.create(name="alex", age=20)
# User.objects.all() -> QuerySet
# exists(), check if have 1 or > object
# users = User.objects.get(name='alex')
# users = User.objects.raw("SELECT * FROM home_user where home_user.name= 'alex' ")
# users = User.objects.all().filter(age__range=(15, 25))
# for user in users:
#     print(f'#{user.id} {user.name}, {user.age}')


# result = User.objects.bulk_create(name="alex", age=20)
# print(result)



def index(request: WSGIRequest):
    # data = {
    #     "name": request.user,
    #     "message": "message from back-end"
    # }
    # person = Person("Alex", 20, [32, 12, 55])
    # ls = [32, 12, 55]
    # user = {"name": "Alex", "age":20}
    # addr = ("Street", 23,1)
    # data = {"user": user, "customers": ls, "address": addr,
    #         "message": "message from back-end"}
    return render(request, "index.html")
                  # context={"person": person, "data": "22.02.2002"})


def users_creat(request: WSGIRequest):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        phone = request.POST.get("phone")
        User.objects.create(name=name, age=age, phone=phone)
        return redirect('/users')
    return redirect('/users')


def user_delete(request):
    id = request.POST.get('id')
    User.objects.delete(id=id)
    return redirect('/users')


def user_get(request):
    users = User.objects.all()
    return render(request, 'user.html', context={'users': users})


def about(request):
    return render(request, 'about.html')


def persons(request: WSGIRequest):
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
