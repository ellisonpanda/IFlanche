from django import forms
from .models import Perfil, CardapioSemanal
from django.contrib.auth.models import User

class PerfilForm(forms.ModelForm):
     class Meta:
        model = Perfil
        fields = ['nome_completo', 'apelido', 'foto']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'apelido': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AdminRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

# Este é o novo formulário para o painel de admin (cantina)
class CardapioSemanalForm(forms.ModelForm):
    class Meta:
        model = CardapioSemanal
        fields = [
            'semana',
            'manha_segunda', 'tarde_segunda',
            'manha_terca', 'tarde_terca',
            'manha_quarta', 'tarde_quarta',
            'manha_quinta', 'tarde_quinta',
            'manha_sexta', 'tarde_sexta',
        ]
        
        # Este 'widgets' faz os campos parecerem mais bonitos (estilo Bootstrap)
        # E também organiza os campos em caixas de texto maiores (Textarea)
        widgets = {
            'semana': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Ex: Semana de 17/11 a 21/11'}),
            
            'manha_segunda': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'tarde_segunda': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            
            'manha_terca': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'tarde_terca': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            
            'manha_quarta': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'tarde_quarta': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            
            'manha_quinta': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'tarde_quinta': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            
            'manha_sexta': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'tarde_sexta': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }