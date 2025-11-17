from django.urls import path
from . import views
from core.views import CustomLogoutView

urlpatterns = [
    # 1. Página de Login
    path('', views.suap_login, name='index'),
    
    # 2. Página do Cardápio
    path('cardapio/', views.cardapio_semana, name='cardapio_semana'),
    
    # 3. Página de Logout
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    # --- Deixe o resto aqui, mas não vamos usá-los agora ---
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('dashboard/', views.usuario_dashboard, name='usuario_dashboard'),
    path('notificacoes/', views.notificacoes_usuario, name='notificacoes_usuario'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('painel-admin/', views.painel_admin, name='painel_admin'),
    path('registrar-admin/', views.registrar_admin, name='registrar_admin'),
]