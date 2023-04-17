from mysite.newprog.forms import RegisterForm

from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required

from mysite.newprog.models import Product


def index(request):
    # author = Author.objects.create(name='John Doe', email='alex@gmail.com')
    # book1 = Book.objects.create(title='Book', author=author)
    # book2 = Book.objects.create(title='Book', author=author)
    # author.books.add(book1,book2)
    # author.save()
    # book.save()

    # author = Author.objects.get(id=3)
    # books = author.books.all()
    # print(books)
    #
    # author.name = 'Deker'
    # author.save()
    #
    # book.title = 'My book'
    # book.save()
    # return HttpResponse(f'<h1>book</h1>')

    return render(request, "index.html")


def product_list(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def profile(request):
    print(request.user)
    return render(request, 'profile.html', {"user": request.user})


def logout(request):
    logout(request)
    return redirect('index')
