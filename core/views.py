import requests
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

from .models import CardapioSemanal

def cardapio_semana(request):
    cardapio = CardapioSemanal.objects.last()  # Último cadastro
    return render(request, 'cardapio_dia.html', {'cardapio': cardapio})


def suap_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        auth_url = "https://suap.ifrn.edu.br/api/v2/autenticacao/token/"
        response = requests.post(auth_url, json={"username": username, "password": password})

        if response.status_code == 200:
            access_token = response.json()['access']

            headers = {"Authorization": f"Bearer {access_token}"}
            user_info = requests.get(
                "https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/",
                headers=headers
            ).json()

            nome = user_info['nome_usual']
            matricula = user_info['matricula']

            user, created = User.objects.get_or_create(username=matricula)
            user.first_name = nome
            user.set_unusable_password()
            user.save()

            login(request, user)
            return redirect('cardapio')

        else:
            return render(request, 'index.html', {'error': 'Login inválido!'})

    return render(request, 'index.html')


def logout_view(request):
    logout(request)
    return redirect('index')
