from django.urls import path
from . import views

urlpatterns = [
    path('cardapio/', views.cardapio_dia, name='cardapio_dia'),
    path('cardapio', views.cardapio_dia),
]
