from django.contrib import admin

from .models.campeonato import Campeonato
from .models.jogador import Jogador
from .models.partida import Partida
from .models.quadras import Horario, Quadra
from .models.time import Time


@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ['cpf', 'nome', 'criado_em']


@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'abreviacao', 'criado_em']


@admin.register(Campeonato)
class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ['nome']


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ['hora']


@admin.register(Quadra)
class QuadraAdmin(admin.ModelAdmin):
    list_display = ['nome']


@admin.register(Partida)
class PartidaAdmin(admin.ModelAdmin):
    list_display = ['time_casa', 'time_fora']
