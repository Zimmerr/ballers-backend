from django.urls import include, path
from rest_framework import routers

from .api.views.campeonato import CampeonatoViewSet
from .api.views.jogador import JogadorViewSet
from .api.views.time import TimeViewSet

router = routers.DefaultRouter()

router.register("jogadores", JogadorViewSet)
router.register("times", TimeViewSet)
router.register("campeonatos", CampeonatoViewSet)

urlpatterns = [path("", include(router.urls))]
