from rest_framework import permissions, viewsets

from ...models.time import Time
from ..serializers.time import TimeCreateSerializer, TimeSerializer


class TimeViewSet(viewsets.ModelViewSet):
    lookup_field = "uuid"
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return TimeSerializer
        else:
            return TimeCreateSerializer
