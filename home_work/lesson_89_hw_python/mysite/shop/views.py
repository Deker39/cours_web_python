from django.shortcuts import *
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
import datetime


# TODO если пользователь авторизован то сменить адрес на лисную страницу


def index(request):
    catalog = CatalogProduct.objects.all()
    product = Product.objects.all()
    product_day = ProductsDay.objects.all()

    context = {
        'title': 'main page',
        'list_catalog': catalog.values(),
        'list_product': product.values(),
        'list_product_day': product_day.values(),
    }
    return render(request, 'main_page.html', context=context)


def signin(request):
    context = {
        'title': 'sign in',
    }
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            log_user = User()
            log_user.email = request.POST.get('emailAddressInput')
            log_user.password = request.POST.get('passwordInput')

            user = authenticate(username=log_user.email, password=log_user.password)
            if user is not None:
                login(request, user)
                context['user'] = False
                return redirect('index')
            else:
                if not User.objects.filter(email=log_user.email):
                    context['emailNotExists'] = f'{log_user.email}'
                else:
                    context['emailForNotCorrectPass'] = log_user.email

    return render(request, 'entrance_page.html', context=context)


def register(request):
    context = {
        'title': 'sign up',
    }

    if request.method == "POST":
        new_user = User()
        new_user.first_name = request.POST.get('firstNameInput')
        new_user.last_name = request.POST.get('lastNameInput')
        new_user.email = request.POST.get('emailAddressInput')
        new_user.password = request.POST.get('passwordInput')
        check_user = User.objects.filter(Q(first_name=new_user.first_name) &
                                         Q(last_name=new_user.last_name))
        if check_user:
            context['firstAndLastNameToExists'] = f'{new_user.first_name} {new_user.last_name}'
            return render(request, 'sign in.html', context=context)
        else:
            user = User.objects.create_user(username=new_user.email, password=new_user.password, email=new_user.email)
            user.save()
            new_user.save()
            return redirect('index',)

    return render(request, 'entrance_page.html', context=context)


def signout(request):
    pass


def personal_info(request):
    context = {

    }
    return render(request, 'personal_page.html', context=context)

#     name_menu = ['show']
#     url_menu = ['show news']
#     list_menu = [[name, url] for name, url in zip(name_menu, url_menu)]
#     context = {
#         'title': 'sign out',
#         'params_page': params_page.values(),
#         'list_menu': list_menu
#     }
#     logout(request)
#     return render(request, "sign out.html", context=context)

def change_password(request):
    pass
