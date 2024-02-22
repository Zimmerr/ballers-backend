from rest_framework import permissions, viewsets

from ...models.campeonato import Campeonato
from ..serializers.campeonato import (CampeonatoCreateSerializer,
                                      CampeonatoSerializer)


class CampeonatoViewSet(viewsets.ModelViewSet):
    lookup_field = "uuid"
    queryset = Campeonato.objects.all()
    serializer_class = CampeonatoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return CampeonatoSerializer
        else:
            return CampeonatoCreateSerializer
