from rest_framework import serializers

from ...models.jogador import Jogador
from ...models.time import Time
from ..serializers.jogador import JogadorSerializer


class TimeSerializer(serializers.ModelSerializer):
    jogadores = JogadorSerializer(many=True)

    class Meta:
        model = Time
        fields = ['uuid', 'nome', 'abreviacao', 'apelido', 'jogadores']


class TimeCreateSerializer(serializers.ModelSerializer):
    jogadores = serializers.SlugRelatedField(
        slug_field="uuid",
        required=True,
        queryset=Jogador.objects.filter(ativo=True),
        many=True
    )

    class Meta:
        model = Time
        exclude = ("id",)
