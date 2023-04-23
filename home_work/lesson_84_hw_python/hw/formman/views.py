from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from .models import *


def index(request):
    if request.method == "POST":
        form = ValueFormMan(request.POST)
        form.first_name = request.POST.get('firstNameInput')
        form.middle_name = request.POST.get('middleNameInput')
        form.last_name = request.POST.get('lastNameInput')
        form.city = request.POST.get('cityInput')
        result = ValueFormMan.objects.filter(Q(first_name=form.first_name) &
                                             Q(middle_name=form.middle_name) &
                                             Q(last_name=form.last_name) &
                                             Q(city=form.city))

        if result:
            return render(request, 'formman.html', {'result': result})
    else:
        form = ValueFormMan()

    return render(request, 'formman.html')
