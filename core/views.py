from django.shortcuts import render
from .models import CardapioSemanal

def cardapio_semana(request):
    cardapio = CardapioSemanal.objects.last()  # Último cadastro
    return render(request, 'cardapio_dia.html', {'cardapio': cardapio})
