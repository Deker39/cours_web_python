from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloworld),
    path('/<str:lang>', views.helloworld),
]