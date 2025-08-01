from django import forms
from .models import Perfil

class PerfilForm(forms.ModelForm):
     class Meta:
        model = Perfil
        fields = ['nome_completo', 'apelido', 'foto']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'apelido': forms.TextInput(attrs={'class': 'form-control'}),
        }
