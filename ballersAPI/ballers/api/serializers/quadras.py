from rest_framework import serializers

from ...models.quadras import Horario, Quadra


class QuadraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quadra
        exclude = ("id",)


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        exclude = ("id",)
