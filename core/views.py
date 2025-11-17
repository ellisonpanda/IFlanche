from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from .models import CardapioSemanal  # Importa SÓ o que precisamos

# ==========================================================
# 1. PÁGINA DE LOGIN
# ==========================================================
def suap_login(request):
    # Se o usuário já está logado, não pode ver o login
    if request.user.is_authenticated:
        return redirect('cardapio_semana')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # IMPORTANTE: Estamos usando o login do Django para testar.
        # Use o superusuário que você criou (ex: 'stephanny').
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('cardapio_semana') # Redireciona para o cardápio
        else:
            messages.error(request, 'Matrícula ou senha inválida.')
            return redirect('index') # Volta para a página de login
    
    # Se não for POST, apenas mostra a página de login
    return render(request, 'core/login.html')

# ==========================================================
# 2. PÁGINA DO CARDÁPIO
# ==========================================================
@login_required(login_url='index') # Protege a página, se não logar volta para 'index'
def cardapio_semana(request):
    # Busca o cardápio. Se não existir (id=1), ele cria um vazio.
    # Isso IMPEDE o site de quebrar se o banco estiver vazio.
    cardapio, created = CardapioSemanal.objects.get_or_create(id=1)
    
    context = {
        'cardapio': cardapio
    }
    return render(request, 'core/cardapio_semana.html', context)

# ==========================================================
# 3. PÁGINA DE LOGOUT
# ==========================================================
class CustomLogoutView(LogoutView):
    next_page = '/' # Volta para o login após sair

# ==========================================================
# DEIXE AS OUTRAS FUNÇÕES VAZIAS POR ENQUANTO
# (Não vamos mexer em perfil, dashboard, etc. para não quebrar)
# ==========================================================
@login_required(login_url='index')
def perfil_usuario(request):
    return render(request, 'core/perfil_usuario.html') # Crie esse HTML se precisar

@login_required(login_url='index')
def usuario_dashboard(request):
    return redirect('cardapio_semana') # Redireciona tudo para o cardápio

@login_required(login_url='index')
def notificacoes_usuario(request):
    return render(request, 'core/notificacoes.html') # Crie esse HTML se precisar

def admin_login(request):
    return render(request, 'core/admin_login.html') # Crie esse HTML se precisar

@login_required(login_url='index')
def painel_admin(request):
    return render(request, 'core/painel_admin.html') # Crie esse HTML se precisar

def registrar_admin(request):
    return render(request, 'core/registrar_admin.html') # Crie esse HTML se precisar