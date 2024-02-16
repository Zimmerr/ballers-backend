from django.contrib import admin

from .models.jogador import Jogador
from .models.time import Time


@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ['cpf', 'nome', 'criado_em']


@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'abreviacao', 'criado_em']
