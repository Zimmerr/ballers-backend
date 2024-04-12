from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from ...models.partida import Partida
from ..serializers.partida import PartidaCreateSerializer, PartidaSerializer


class PartidaViewSet(viewsets.ModelViewSet):
    lookup_field = "uuid"
    queryset = Partida.objects.all()
    serializer_class = PartidaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return PartidaSerializer
        else:
            return PartidaCreateSerializer

    def destroy(self, request, *args, **kwargs):
        partida = self.get_object()
        if partida.finalizada is True:
            return Response('Não é possível deletar uma partida que já foi realizada', status.HTTP_400_BAD_REQUEST)
        else:
            partida.delete()
            return Response(data='Partida cancelada com sucesso!')
