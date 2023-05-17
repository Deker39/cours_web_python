from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),




    path("register/", views.register, name="register"),
    path("change_password/", views.change_password, name="change_password"),
    path("login/", views.signin, name="login"),
    path("logout/", views.signout, name="logout"),
]