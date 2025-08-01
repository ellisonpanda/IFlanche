import requests
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CardapioSemanal, Perfil
from .forms import PerfilForm


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
            return redirect('perfil')  # Redireciona para a página do perfil

        else:
            messages.error(request, 'Você não tem acesso ao SUAP ou suas credenciais estão incorretas.')
            return redirect('index')

    return render(request, 'index.html')


def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def perfil_usuario(request):
    # Pega ou cria o perfil do usuário
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('perfil')  # Mantém na página de perfil após salvar
        else:
            messages.error(request, 'Erro ao atualizar o perfil. Por favor, corrija os erros.')
    else:
        form = PerfilForm(instance=perfil)

    context = {
        'usuario': request.user,
        'perfil': perfil,
        'form': form,
    }
    return render(request, 'perfil.html', context)
