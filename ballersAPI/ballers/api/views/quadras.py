from rest_framework import permissions, viewsets

from ...models.quadras import Horario, Quadra
from ..serializers.quadras import HorarioSerializer, QuadraSerializer


class QuadraViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = "uuid"
    queryset = Quadra.objects.all()
    serializer_class = QuadraSerializer
    permission_classes = [permissions.IsAuthenticated]


class HorarioViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = "uuid"
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    permission_classes = [permissions.IsAuthenticated]
