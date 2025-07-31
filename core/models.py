from django.db import models
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
