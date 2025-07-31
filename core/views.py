from django.shortcuts import render
from .models import Lanche

def cardapio_dia(request):
    dias_semana = ['SEG', 'TER', 'QUA', 'QUI', 'SEX']

    cardapio = {}

    for dia in dias_semana:
        lanches_manha = Lanche.objects.filter(dia_semana=dia, periodo='MANHA')
        lanches_tarde = Lanche.objects.filter(dia_semana=dia, periodo='TARDE')
        cardapio[dia] = {
            'manha': lanches_manha,
            'tarde': lanches_tarde,
        }

    context = {'cardapio': cardapio}
    return render(request, 'cardapio_dia.html', context)
