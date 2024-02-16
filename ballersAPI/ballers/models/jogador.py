from django.core.validators import MinLengthValidator
from django.db import models

from .base import Ativavel, ModeloBase


class Jogador(ModeloBase, Ativavel):
    nome = models.CharField("Nome", max_length=150)
    altura = models.IntegerField("Altura (em cm)")
    data_nasc = models.DateField("Data de Nascimento")
    cpf = models.CharField(
        max_length=11,
        unique=True,
        validators=[MinLengthValidator(11)],
    )

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = "Jogador"
        verbose_name_plural = "Jogadores"
