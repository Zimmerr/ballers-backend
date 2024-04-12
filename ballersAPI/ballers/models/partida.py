from django.db import models

from .base import ModeloBase
from .campeonato import Campeonato
from .quadras import Horario, Quadra
from .time import Time


class Partida(ModeloBase):
    time_casa = models.ForeignKey(Time, on_delete=models.PROTECT, related_name="partidas_casa")
    time_fora = models.ForeignKey(Time, on_delete=models.PROTECT, related_name="partidas_fora")
    campeonato = models.ForeignKey(Campeonato, on_delete=models.PROTECT, blank=True, null=True)

    data = models.DateField("Data")
    horario = models.ForeignKey(Horario, on_delete=models.PROTECT)
    quadra = models.ForeignKey(Quadra, on_delete=models.PROTECT)

    finalizada = models.BooleanField(default=False)
    gols_casa = models.IntegerField(blank=True, null=True)
    gols_fora = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.time_casa.abreviacao} x {self.time_fora.abreviacao}"

    class Meta:
        verbose_name = "Partida"
        verbose_name_plural = "Partidas"
        constraints = [
            models.UniqueConstraint(
                fields=['data', 'horario', 'quadra'], name='exclusividade_quadra'
            )
        ]
