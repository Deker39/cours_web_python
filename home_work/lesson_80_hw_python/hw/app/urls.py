from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.hello),
    path('day week', views.day_week),
    path('quotes', views.quotes),
    path('', views.index)
]
