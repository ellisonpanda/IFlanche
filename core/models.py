from django.db import models
from django.contrib.auth.models import User
DIAS_SEMANA = [
    ('segunda', 'Segunda-feira'),
    ('terca', 'Terça-feira'),
    ('quarta', 'Quarta-feira'),
    ('quinta', 'Quinta-feira'),
    ('sexta', 'Sexta-feira'),
]

class CardapioSemanal(models.Model):
    semana = models.CharField(max_length=20)

    # Manhã
    manha_segunda = models.CharField(max_length=100)
    manha_terca = models.CharField(max_length=100)
    manha_quarta = models.CharField(max_length=100)
    manha_quinta = models.CharField(max_length=100)
    manha_sexta = models.CharField(max_length=100)

    # Tarde
    tarde_segunda = models.CharField(max_length=100)
    tarde_terca = models.CharField(max_length=100)
    tarde_quarta = models.CharField(max_length=100)
    tarde_quinta = models.CharField(max_length=100)
    tarde_sexta = models.CharField(max_length=100)

    def __str__(self):
        return f"Semana {self.semana}"

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=100)
    apelido = models.CharField(max_length=50, blank=True, null=True)  # opcional
    foto = models.ImageField(upload_to='perfil_fotos/', blank=True, null=True)

    def __str__(self):
        return self.nome_completo or self.user.username

class Notificacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notificacoes')
    mensagem = models.TextField()
    lida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {'Lida' if self.lida else 'Não lida'}"