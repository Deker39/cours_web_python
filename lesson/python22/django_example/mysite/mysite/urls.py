"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from home import views as home

urlpatterns = [
    #  ^ - start
    #  $ - end
    #  ^$
    #  + > 1
    #  ? 0 or 1
    # {n} - n -elem
    # {n,m} - n-m elem
    # . -
    # \d+ - >1 num
    # \D+ - >1 !num
    # \w+ - >1 letters

    path('admin/', admin.site.urls),
    # re_path(r'^home/contact|phone|addres', home.contact),
    # re_path(r'^home$', home.index),
    # re_path(r'^products/\d+/$', home.products, kwargs={'id':543}),
    # path('user/<str:name>', home.user),
    re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)$', home.user),
    re_path(r'^products/[1-9]{2}/$', home.products, kwargs={'id': 543}),
    re_path(r'^home/', include('home.urls')),
    path('person/', home.persons),
    path('', home.index)


]
