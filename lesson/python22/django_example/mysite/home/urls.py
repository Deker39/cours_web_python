from django.urls import path

from home import views

urlpatterns = [
    path('', views.home),
    path('/lviv', views.lviv),
    path('/kiev', views.kiev)
]