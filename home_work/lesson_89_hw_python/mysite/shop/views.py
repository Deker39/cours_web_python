import re
from django.shortcuts import *
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import JsonResponse
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


def basket(request):

    context = {
        'title': 'basket',
    }

    user_id = ShopUser.objects.get(email=request.user.username).id
    check_order = Order.objects.filter(Q(user_id=user_id) & Q(complete=0)).first()
    if check_order:
        order = check_order
        list_order = OrdersList.objects.filter(order=order)
        list_product = Product.objects.filter(id__in=list_order.values('product_id'))
        total_amount = sum([i.calculate_item_total() for i in list_order])
        order.total_amount = total_amount
        order.save()
        context['order'] = order
        context['list_order'] = list_order
        context['list_product'] = list_product
        context['checkOrder'] = True
    else:
        context['checkOrder'] = False

    return render(request, 'basket_page.html', context=context)


def checkout(request):
    user_shop = ShopUser.objects.get(email=request.user.username)
    order = Order.objects.filter(Q(user_id=user_shop.id) & Q(complete=0)).first()
    if order:

        list_order = OrdersList.objects.filter(order=order)
        list_product = Product.objects.filter(id__in=list_order.values('product_id'))
        if request.method == "POST":
            for prod in list_product:
                prod_key = ProductKey()
                prod_key.order_id = order.id
                prod_key.products_id = prod.id
                prod_key.key = generate_rand_key()
                prod_key.save()
            return redirect(successful)

        context = {
            'title': 'checkout',
            'user': user_shop,
            'order': order,
            'list_product': list_product,


        }
        return render(request, 'checkout _page.html', context=context)
    else:
        return redirect(basket)


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
    if request.method == 'POST':
        user_id = ShopUser.objects.get(email=request.user.username).id
        check_order = Order.objects.filter(Q(user_id=user_id) & Q(complete=0)).first()
        print(check_order)
        if check_order:
            order = check_order
        else:
            order = Order()

        order.complete = False
        order.user_id = user_id
        order.save()
        product_id = request.POST.get('product_id')
        order_list = OrdersList()
        order_list.product_id = product_id
        order_list.order_id = order.id
        order_list.save()

    context = {
        'title': f'product {product_cat.title}',
        'list_catalog': catalog,
        'product': product_cat,
        'product_photo': product_photo,
        'product_info': product_info,
        'cat_prduct': cat_prduct,
        'also_product_cat': also_product_cat,

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
    user_id = ShopUser.objects.get(email=request.user.username).id
    order = Order.objects.filter(user_id=user_id, complete=False).last()
    list_order = OrdersList.objects.filter(order=order)
    prod_keys = ProductKey.objects.filter(order=order, products__in=list_order.values('product_id'))
    list_product = Product.objects.filter(id__in=list_order.values('product_id'))
    order.complete = True
    order.save()
    list_game_key = [[prod.title, prod_key.key ] for prod, prod_key in zip(prod_keys, list_product)]
    context = {
        'title': 'successful',
        'list_game_key': list_game_key,
    }
    return render(request, "status_page.html", context=context)


def personal_info(request):
    name_menu = ['personal data', 'basket', 'my orders', 'password change', 'exit', 'delete account']
    url_menu = ['personal data', 'basket', 'checkout', 'change password', 'logout', 'delete account']
    list_menu = [[name, url] for name, url in zip(name_menu, url_menu)]

    context = {
        'personal_list': list_menu

    }
    return render(request, 'user_page.html', context=context)


def change_personal_data(request):
    context = {
        'title': 'personal data'
    }
    return render(request, "personal_page.html", context=context)


def change_password(request):
    user = ShopUser.objects.get(email=request.user.username)
    if request.method == "POST":
        user.password = request.POST.get('passwordInput')
        user.save()
        redirect(successful_change_password)
    context = {
        'title': 'change password',
        'old_pass': user.password
    }
    return render(request, "entrance_page.html", context=context)


def successful_change_password(request):
    context = {
        'title': 'successful change password',
    }
    return render(request, "status_page.html", context=context)
