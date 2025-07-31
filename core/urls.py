from django.urls import path
from .views import cardapio_semana

urlpatterns = [
    path('cardapio/', cardapio_semana, name='cardapio'),
]
