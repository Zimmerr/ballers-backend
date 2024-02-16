from rest_framework import permissions, viewsets
from rest_framework.response import Response

from ...models.jogador import Jogador
from ..serializers.jogador import JogadorSerializer


class JogadorViewSet(viewsets.ModelViewSet):
    lookup_field = "uuid"
    queryset = Jogador.objects.filter(ativo=True)
    serializer_class = JogadorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        jogador = self.get_object()
        jogador.ativo = False
        jogador.save()
        return Response(data='Jogador inativado com sucesso!')
