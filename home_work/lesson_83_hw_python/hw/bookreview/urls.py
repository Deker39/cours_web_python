from django.urls import path
from . import views

urlpatterns = [
    path('add', views.form_add, name='add book'),
    path('successful', views.successful,),
    path('show', views.show, name='show book'),
    path('', views.index_book, name='book'),

]
