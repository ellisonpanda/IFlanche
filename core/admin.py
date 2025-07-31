from django.contrib import admin
from .models import Lanche

@admin.register(Lanche)
class LancheAdmin(admin.ModelAdmin):
    list_display = ['refeicao', 'bebida', 'dia_semana', 'periodo']
    list_filter = ['dia_semana', 'periodo']
    search_fields = ['refeicao', 'bebida']
