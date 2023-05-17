from django.shortcuts import *
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.db.models import Q
import datetime


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
    if request.user.is_authenticated:
        return redirect('/')
    else:
        pass
        # if request.method == "POST":
        #     log_user = UserNews()
        #     log_user.email = request.POST.get('emailAddressInput')
        #     log_user.password = request.POST.get('passwordInput')
        #     check_user = UserNews.objects.filter(Q(email=log_user.email) &
        #                                          Q(ban=1))
        #
        #     if not check_user:
        #         user = authenticate(username=log_user.email, password=log_user.password)
        #         if user is not None:
        #             login(request, user)
        #             return redirect('show news')
        #         else:
        #             if not UserNews.objects.filter(email=log_user.email):
        #                 context['emailNotExists'] = f'{log_user.email}'
        #             else:
        #                 context['emailForNotCorrectPass'] = log_user.email
        #             return render(request, 'sign up.html', context=context)
        #     else:
        #         if check_user.values()[0]['ban_time'].strftime(
        #                 '%d-%m-%Y %H:%M:%S') < datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'):
        #             check_user.update(ban=0)
        #         else:
        #             context['banUserNotExists'] = check_user.values()[0]['ban_time']

    return render(request, 'entrance_page.html', context=context)


def signout(request):
    pass
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

