from django.urls import path
from . import views
from core.views import CustomLogoutView

urlpatterns = [
    path('', views.suap_login, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('cardapio/', views.cardapio_semana, name='cardapio_semana'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('dashboard/', views.usuario_dashboard, name='usuario_dashboard'),
    path('notificacoes/', views.notificacoes_usuario, name='notificacoes_usuario'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('painel-admin/', views.painel_admin, name='painel_admin'),
]
