from django.shortcuts import render


def show(request):
    render(request, '<h1>show book</h1>')
