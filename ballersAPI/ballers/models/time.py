from django.db import models

from .base import ModeloBase
from .jogador import Jogador


class Time(ModeloBase):
    nome = models.CharField("Nome", max_length=150)
    abreviacao = models.CharField("Abreviação", max_length=3)
    apelido = models.CharField("Apelido", max_length=30)
    jogadores = models.ManyToManyField(Jogador)

    def __str__(self):
        return f"{self.abreviacao} - {self.nome}"

    class Meta:
        verbose_name = "Time"
        verbose_name_plural = "Times"
