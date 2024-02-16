from django.urls import include, path
from rest_framework import routers

from .api.views.jogador import JogadorViewSet
from .api.views.time import TimeViewSet

router = routers.DefaultRouter()

router.register("jogadores", JogadorViewSet)
router.register("times", TimeViewSet)

urlpatterns = [path("", include(router.urls))]
