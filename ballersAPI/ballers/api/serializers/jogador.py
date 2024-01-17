from rest_framework import serializers

from ...models.jogador import Jogador


class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = ['id', 'nome', 'altura', 'data_nasc', 'cpf']
