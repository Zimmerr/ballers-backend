from django.contrib import admin

from .models.jogador import Jogador


@admin.register(Jogador)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['cpf', 'nome', 'criado_em']
