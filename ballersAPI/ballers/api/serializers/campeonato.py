from rest_framework import serializers

from ...models.campeonato import Campeonato
from ...models.time import Time
from ..serializers.time import TimeSerializer


class CampeonatoSerializer(serializers.ModelSerializer):
    times = TimeSerializer(many=True)

    class Meta:
        model = Campeonato
        fields = ['uuid', 'nome', 'descricao', 'times']


class CampeonatoCreateSerializer(serializers.ModelSerializer):
    times = serializers.SlugRelatedField(
        slug_field="uuid",
        required=True,
        queryset=Time.objects.all(),
        many=True
    )

    class Meta:
        model = Campeonato
        exclude = ("id",)
