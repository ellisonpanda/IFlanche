from django import forms
from .models import Perfil
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
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']