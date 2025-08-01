import requests
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CardapioSemanal, Perfil
from .forms import PerfilForm
from .models import Notificacao
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


def cardapio_semana(request):
    cardapio = CardapioSemanal.objects.last()
    return render(request, 'cardapio_dia.html', {'cardapio': cardapio})


def suap_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        auth_url = "https://suap.ifrn.edu.br/api/v2/autenticacao/token/"

        try:
            response = requests.post(auth_url, json={"username": username, "password": password}, timeout=5)
        except requests.RequestException:
            messages.error(request, 'Erro de conexão ao SUAP. Tente novamente mais tarde.')
            return redirect('index')

        if response.status_code == 200:
            access_token = response.json().get('access')
            headers = {"Authorization": f"Bearer {access_token}"}

            try:
                user_info = requests.get(
                    "https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/", 
                    headers=headers, timeout=5
                ).json()
            except requests.RequestException:
                messages.error(request, 'Erro ao obter dados do usuário. Tente novamente.')
                return redirect('index')

            nome = user_info.get('nome_usual', '')
            matricula = user_info.get('matricula', '')

            user, created = User.objects.get_or_create(username=matricula)
            user.first_name = nome
            user.set_unusable_password()
            user.save()

            login(request, user)
            return redirect('perfil_usuario')  # redireciona para a página do perfil

        else:
            messages.error(request, 'Você não tem acesso ao SUAP ou suas credenciais estão incorretas.')
            return redirect('index')

    return render(request, 'index.html')


def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def perfil_usuario(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    # Se o perfil foi criado agora e não tem nome completo, preenche com o primeiro nome do user
    if created and not perfil.nome_completo:
        perfil.nome_completo = request.user.first_name
        perfil.save()

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('usuario_dashboard')
        else:
            print("Erros no formulário de perfil:", form.errors)  # Debug: imprime erros no terminal
    else:
        form = PerfilForm(instance=perfil)

    return render(request, 'perfil.html', {'form': form})




@login_required
def usuario_dashboard(request):
    # Busca perfil associado ao usuário
    perfil = getattr(request.user, 'perfil', None)

    context = {
        'user': request.user,
        'profile': perfil,
    }
    return render(request, 'usuario_dashboard.html', context)

@login_required
def notificacoes_usuario(request):
    notificacoes = Notificacao.objects.filter(usuario=request.user).order_by('-criada_em')
    return render(request, 'notificacoes.html', {'notificacoes': notificacoes})

def dashboard_usuario(request):
    user = request.user
    notificacoes_nao_lidas = Notificacao.objects.filter(usuario=user, lida=False).count()

    context = {
        'notificacoes_nao_lidas': notificacoes_nao_lidas,
        'user': user,
    }

    return render(request, 'usuario_dashboard.html', context)

    
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'usuario/dashboard.html'

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Você saiu com sucesso. Até logo! 👋")
        return super().dispatch(request, *args, **kwargs)
