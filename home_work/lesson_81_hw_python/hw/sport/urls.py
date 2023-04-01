from django.urls import path
from . import views

urlpatterns = [
    path('', views.sport),
    path('/<str:type_sport>', views.sport),
]