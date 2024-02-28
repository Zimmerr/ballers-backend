from django.db import models

from .base import ModeloBase


class Horario(ModeloBase):
    hora = models.TimeField(unique=True)

    def __str__(self):
        return f"{self.hora}"

    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"


class Quadra(ModeloBase):
    nome = models.CharField("Nome da Quadra", max_length=50, unique=True)

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = "Quadra"
        verbose_name_plural = "Quadras"
