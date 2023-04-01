import random

from django.shortcuts import render
from django.http import *
from datetime import datetime

weekdays = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}


def index(request):
    return HttpResponse('<h1>Write a path => </h1>')


def hello(request):
    return HttpResponse('<h1>Hello, world</h1>')


def day_week(request):
    day = datetime.today().isoweekday()
    return HttpResponse(f'<h1>Today: {weekdays[day]}</h1>')


def quotes(request):
    ls = ['quotes1', 'quotes2', 'quotes3', 'quotes4', 'quotes5', 'quotes6']
    return HttpResponse(f'<h1>Random quotes: {ls[random.randint(0,len(ls))]}</h1>')
