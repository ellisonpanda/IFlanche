from django.db import models
class Lanche(models.Model):
    DIA_SEMANA_CHOICES = [
        ('SEG', 'Segunda-feira'),
        ('TER', 'Terça-feira'),
        ('QUA', 'Quarta-feira'),
        ('QUI', 'Quinta-feira'),
        ('SEX', 'Sexta-feira'),
    ]

    PERIODO_CHOICES = [
        ('MANHA', 'Manhã'),
        ('TARDE', 'Tarde'),
    ]

    dia_semana = models.CharField(max_length=3, choices=DIA_SEMANA_CHOICES)
    periodo = models.CharField(max_length=5, choices=PERIODO_CHOICES)
    refeicao = models.CharField(max_length=100)
    bebida = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.get_dia_semana_display()} - {self.refeicao} + {self.bebida} ({self.get_periodo_display()})"
