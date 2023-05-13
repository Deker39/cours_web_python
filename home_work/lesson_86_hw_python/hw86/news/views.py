import datetime

from django.shortcuts import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *

global params_page
params_page = ParamsProject.objects.all()  # TODO сделать так чтобы он работал через base


def show_news(request):
    news = NewsPost.objects.all()
    imgs = ImageNewsPost.objects.all()
    comments = CommentPost.objects.all()
    authors = UserNews.objects.all()

    if request.user.is_authenticated:
        name_menu = ['show', 'sign out']
        url_menu = ['show news', 'sign out']
        if request.method == "POST":
            new_comment = CommentPost()
            new_comment.auth = UserNews.objects.get(email=request.user.email)
            new_comment.post = NewsPost.objects.get(id=request.POST.get('postInput'))
            new_comment.content = request.POST.get('commentInput')
            False if new_comment.content == '' or new_comment.content == ' ' else new_comment.save()
    else:
        name_menu = ['show', 'sign in', 'sign up']
        url_menu = ['show news', 'sign in', 'sign up']

    list_menu = [[name, url] for name, url in zip(name_menu, url_menu)]

    context = {
        'title': 'show news',
        'params_page': params_page.values(),
        'list_menu': list_menu,
        'news': news.values(),
        'imgs': imgs.values(),
        'comments': comments.values(),
        'authors': authors.values(),
        'authorizationUser': True if request.user.is_authenticated else False
    }
    return render(request, 'show.html', context=context)


def sign_in(request):
    name_menu = ['show', 'sign in', 'sign up']
    url_menu = ['show news', 'sign in', 'sign up']
    list_menu = [[name, url] for name, url in zip(name_menu, url_menu)]

    context = {
        'title': 'sign in',
        'params_page': params_page.values(),
        'list_menu': list_menu
    }
    if request.method == "POST":
        new_user = UserNews()
        new_user.first_name = request.POST.get('firstNameInput')
        new_user.last_name = request.POST.get('lastNameInput')
        new_user.email = request.POST.get('emailAddressInput')
        new_user.password = request.POST.get('passwordInput')
        new_user.ban = 0
        new_user.ban_time = datetime.date.today()
        check_user = UserNews.objects.filter(Q(first_name=new_user.first_name) &
                                             Q(last_name=new_user.last_name))
        if check_user:
            context['firstAndLastNameToExists'] = f'{new_user.first_name} {new_user.last_name}'
            return render(request, 'sign in.html', context=context)
        else:
            user = User.objects.create_user(username=new_user.email, password=new_user.password, email=new_user.email)
            user.save()
            new_user.save()
            return redirect('show news')

    return render(request, 'sign in.html', context=context)


def sign_up(request):
    name_menu = ['show', 'sign in', 'sign up']
    url_menu = ['show news', 'sign in', 'sign up']
    list_menu = [[name, url] for name, url in zip(name_menu, url_menu)]

    context = {
        'title': 'sign up',
        'params_page': params_page.values(),
        'list_menu': list_menu
    }
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            log_user = UserNews()
            log_user.email = request.POST.get('emailAddressInput')
            log_user.password = request.POST.get('passwordInput')
            check_user = UserNews.objects.filter(Q(email=log_user.email) &
                                                 Q(ban=1))

            if not check_user:
                user = authenticate(username=log_user.email, password=log_user.password)
                if user is not None:
                    login(request, user)
                    return redirect('show news')
                else:
                    if not UserNews.objects.filter(email=log_user.email):
                        context['emailNotExists'] = f'{log_user.email}'
                    else:
                        context['emailForNotCorrectPass'] = log_user.email
                    return render(request, 'sign up.html', context=context)
            else:
                if check_user.values()[0]['ban_time'].strftime(
                        '%d-%m-%Y %H:%M:%S') < datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'):
                    check_user.update(ban=0)
                else:
                    context['banUserNotExists'] = check_user.values()[0]['ban_time']

    return render(request, 'sign up.html', context=context)


def sign_out(request):
    name_menu = ['show']
    url_menu = ['show news']
    list_menu = [[name, url] for name, url in zip(name_menu, url_menu)]
    context = {
        'title': 'sign out',
        'params_page': params_page.values(),
        'list_menu': list_menu
    }
    logout(request)
    return render(request, "sign out.html", context=context)
