from django.urls import include, path
from rest_framework import routers

from .api.views.campeonato import CampeonatoViewSet
from .api.views.jogador import JogadorViewSet
from .api.views.partida import PartidaViewSet
from .api.views.quadras import HorarioViewSet, QuadraViewSet
from .api.views.time import TimeViewSet

router = routers.DefaultRouter()

router.register("jogadores", JogadorViewSet)
router.register("times", TimeViewSet)
router.register("campeonatos", CampeonatoViewSet)
router.register("partidas", PartidaViewSet)
router.register("horarios", HorarioViewSet)
router.register("quadras", QuadraViewSet)

urlpatterns = [path("", include(router.urls))]
