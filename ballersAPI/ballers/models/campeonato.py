from django.db import models

from .base import ModeloBase
from .time import Time


class Campeonato(ModeloBase):
    nome = models.CharField("Nome", max_length=150)
    descricao = models.CharField("Descrição", max_length=1000)
    times = models.ManyToManyField(Time)

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = "Campeonato"
        verbose_name_plural = "Campeonatos"
