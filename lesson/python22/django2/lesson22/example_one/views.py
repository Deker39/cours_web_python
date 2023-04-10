from django.shortcuts import render, redirect

from .models import Person


def index(request):
    persons = Person.objects.all()
    return render(request, "index.html", {'persons': persons})


def create(request):
    person = Person()
    person.name = request.POST.get('name')
    person.age = request.POST.get('age')
    person.save()
    return redirect('/')


def edit(request, id, methods=['POST']):
    try:
        person = Person.objects.get(id=id)
        if request.method == 'POST':
            person.name = request.POST.get('name')
            person.age = request.POST.get('age')
            person.save()
            return redirect('/')
        else:
            return render(request, 'edit.html', {'person': person})


    except Person.DoesNotExist:
        return render(request, 'edit.html', {'message': 'Person dose not exists'})


def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return redirect('/')
    except Person.DoesNotExist:
        return render(request, 'edit.html', {'message': 'Person not found'})
