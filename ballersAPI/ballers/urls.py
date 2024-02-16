from django.urls import include, path
from rest_framework import routers

from .api.views.jogador import JogadorViewSet

router = routers.DefaultRouter()

router.register("jogadores", JogadorViewSet)

urlpatterns = [path("", include(router.urls))]
