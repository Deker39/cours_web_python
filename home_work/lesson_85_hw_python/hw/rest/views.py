import json

from django.http import *
from django.shortcuts import render, redirect
from .models import *


menu = ['add', 'show', 'search']


def add_rest(request):
    if request.method == "POST":
        form = infoRestModel()
        form.name = request.POST.get('nameRestInput')
        form.specialization = request.POST.get('specializationRestInput')
        form.address = request.POST.get('addressRestInput')
        form.website = request.POST.get('websiteRestInput')
        form.tel = request.POST.get('telRestInput')
        form.save()
        return redirect('./successful')

    context = {
        'title': 'add rest',
        'menu': menu,
    }

    return render(request, 'add_rest.html', context=context)


def successful(request):
    reviews = infoRestModel.objects.latest('id')
    context = {
        'title': 'successful',
        'menu': menu,
        'reviews': reviews
    }
    return render(request, 'successful.html', context=context)


def show(request):
    reviews = infoRestModel.objects.all()
    context = {
        'title': 'show',
        'menu': menu,
        'reviews': reviews
    }
    return render(request, 'show.html', context=context)


def search(request):
    form = infoRestModel(request.POST)
    form.specialization = request.POST.get('specializationRestInput')
    result = infoRestModel.objects.filter(specialization=form.specialization)
    context = {
        'title': 'search',
        'menu': menu,
    }
    if result:
        context.update({'result': result})
        return render(request, 'search.html', context=context)
    else:
        form = infoRestModel()
    return render(request, 'search.html', context=context)


def delete(user_id):
    rest = infoRestModel.objects.get(id=user_id)
    rest.delete()
    return redirect('show')


def edit(request, id):
    rest = infoRestModel.objects.get(id=id)
    if request.method == 'POST':
        rest.name = request.POST.get('nameRestInput')
        rest.specialization = request.POST.get('specializationRestInput')
        rest.address = request.POST.get('addressRestInput')
        rest.website = request.POST.get('websiteRestInput')
        rest.tel = request.POST.get('telRestInput')
        rest.save()
        return redirect('show')
    else:
        context = {
            'title': 'edit',
            'menu': menu,
            'rest': rest
        }
        return render(request, 'edit.html', context=context)

