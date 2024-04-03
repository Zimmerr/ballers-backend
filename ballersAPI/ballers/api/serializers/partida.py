from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from ...models.campeonato import Campeonato
from ...models.partida import Partida
from ...models.quadras import Horario, Quadra
from ...models.time import Time
from ..serializers.campeonato import CampeonatoSerializer
from ..serializers.quadras import HorarioSerializer, QuadraSerializer
from ..serializers.time import TimeSerializer


class PartidaSerializer(serializers.ModelSerializer):
    time_casa = TimeSerializer()
    time_fora = TimeSerializer()
    campeonato = CampeonatoSerializer()
    horario = HorarioSerializer()
    quadra = QuadraSerializer()

    class Meta:
        model = Partida
        exclude = ("id",)


class PartidaCreateSerializer(serializers.ModelSerializer):
    time_casa = serializers.SlugRelatedField(
        slug_field="uuid",
        required=True,
        queryset=Time.objects.all(),
        many=False
    )
    time_fora = serializers.SlugRelatedField(
        slug_field="uuid",
        required=True,
        queryset=Time.objects.all(),
        many=False
    )
    campeonato = serializers.SlugRelatedField(
        slug_field="uuid",
        required=False,
        queryset=Campeonato.objects.all(),
        many=False
    )
    quadra = serializers.SlugRelatedField(
        slug_field="uuid",
        required=True,
        queryset=Quadra.objects.all(),
        many=False
    )
    horario = serializers.SlugRelatedField(
        slug_field="uuid",
        required=True,
        queryset=Horario.objects.all(),
        many=False
    )

    class Meta:
        model = Partida
        exclude = ("id",)
        validators = [
            UniqueTogetherValidator(
                queryset=Partida.objects.all(),
                fields=['quadra', 'horario', 'data']
            )
        ]
