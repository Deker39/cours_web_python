from django.urls import path
from . import views

urlpatterns = [
    path('add', views.form_add, name='add mobile'),
    path('successful', views.successful),
    path('show', views.show, name='show mobile'),
    path('', views.index_mobile, name='mobile'),

]
