from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('/lviv', views.lviv),
    path('/kiev', views.kiev),
    path('/about', views.about)
]