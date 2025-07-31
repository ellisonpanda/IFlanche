from django.urls import path
from . import views

urlpatterns = [
    path('', views.suap_login, name='index'),
    path('logout/', views.logout_view, name='logout'),
   path('cardapio/', views.cardapio_semana, name='cardapio'),
  # já existente
]
