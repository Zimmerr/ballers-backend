from django.contrib import admin

from .models.campeonato import Campeonato
from .models.jogador import Jogador
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
