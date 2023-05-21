import re

from django.shortcuts import *
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
from jinja2 import Environment
import datetime


# TODO если пользователь авторизован то сменить адрес на лисную страницу

def index(request):
    catalog = CatalogProduct.objects.all()
    product_all = Product.objects.all()
    product_day = ProductsDay.objects.all()
    p = []
    for i in product_day:
        p.append(Product.objects.get(id=i.product_id))

    context = {
        'title': 'main page',
        'list_catalog': catalog,
        'list_product': product_all,
        'list_product_day': p,
    }
    return render(request, 'main_page.html', context=context)


def list_catalog(request, cat_slug):
    catalog = CatalogProduct.objects.all()
    product_cat = Product.objects.filter(catalog_id=catalog.get(slug=cat_slug))
    context = {
        'title': f'list catalog {catalog.get(slug=cat_slug)}',
        'list_catalog': catalog,
        'product': product_cat
    }
    return render(request, "search_product.html", context)


def product(request, cat_slug, prod_slug):
    catalog = CatalogProduct.objects.all()
    cat_prduct = CatalogProduct.objects.filter(slug=cat_slug).first()
    product_cat = Product.objects.filter(slug=prod_slug).first()
    product_photo = ProductPhoto.objects.filter(products_id=product_cat.id)
    product_info = ProductSystemRequirement.objects.filter(products_id=product_cat.id).first()
    also_product_cat = Product.objects.filter(catalog_id=catalog.get(slug=cat_slug)).exclude(slug=prod_slug)
    context = {
        'title': f'product {product_cat.title}',
        'list_catalog': catalog,
        'product': product_cat,
        'product_photo': product_photo,
        'product_info': product_info,
        'cat_prduct': cat_prduct,
        'also_product_cat': also_product_cat
    }
    return render(request, "product_page.html", context)


def signin(request):
    context = {
        'title': 'sign in',
    }
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            log_user = ShopUser()
            log_user.email = request.POST.get('emailAddressInput')
            log_user.password = request.POST.get('passwordInput')

            user = authenticate(username=log_user.email, password=log_user.password)
            if user is not None:
                login(request, user)
                context['user'] = False
                return redirect('index')
            else:
                if not ShopUser.objects.filter(email=log_user.email):
                    context['emailNotExists'] = f'{log_user.email}'
                else:
                    context['emailForNotCorrectPass'] = log_user.email

    return render(request, 'entrance_page.html', context=context)


def register(request):
    context = {
        'title': 'sign up',
    }

    if request.method == "POST":
        new_user = ShopUser()
        new_user.first_name = request.POST.get('firstNameInput')
        new_user.last_name = request.POST.get('lastNameInput')
        new_user.email = request.POST.get('emailAddressInput')
        new_user.password = request.POST.get('passwordInput')
        check_user = ShopUser.objects.filter(Q(first_name=new_user.first_name) &
                                             Q(last_name=new_user.last_name))
        if check_user:
            context['firstAndLastNameToExists'] = f'{new_user.first_name} {new_user.last_name}'
            return render(request, 'entrance_page.html', context=context)
        else:
            user = User.objects.create_user(username=new_user.email, password=new_user.password, email=new_user.email)
            user.save()
            new_user.save()
            login(request, user)
            return redirect('index', )

    return render(request, 'entrance_page.html', context=context)


def signout(request):
    context = {
        'title': 'sign out',
    }
    logout(request)
    return render(request, "status_page.html", context=context)


def delete_account(request):
    context = {
        'title': 'delete',
    }

    if request.user.is_authenticated:
        user_del = ShopUser.objects.get(email=request.user.email)
        user = User.objects.get(email=request.user.email)
        context['userDel'] = user_del
        user_del.delete()
        user.delete()

    return render(request, "status_page.html", context=context)


def successful(request):
    context = {
        'title': 'successful',
    }
    return render(request, "status_page.html", context=context)


def personal_info(request):
    name_menu = ['personal data', 'basket', 'my orders', 'password change', 'exit', 'delete account']
    url_menu = ['personal data', 'basket', 'orders', 'change password', 'logout', 'delete account']
    list_menu = [[name, url] for name, url in zip(name_menu, url_menu)]

    context = {
        'personal_list': list_menu

    }
    return render(request, 'user_page.html', context=context)


def orders(request):
    context = {
        'title': 'orders'
    }
    return render(request, "order_page.html", context=context)


def basket_shop(request):
    context = {
        'title': 'basket'
    }
    return render(request, "basket_page.html", context=context)


def change_personal_data(request):
    context = {
        'title': 'personal data'
    }
    return render(request, "personal_page.html", context=context)


def change_password(request):
    context = {
        'title': 'change password'
    }
    return render(request, "personal_page.html", context=context)
