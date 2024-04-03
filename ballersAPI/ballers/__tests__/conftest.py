import pytest
from decouple import config
from pytest_factoryboy import register
from rest_framework.test import APIClient

from ..fixtures.factories.ballers_factory import (CampeonatoFactory,
                                                  HorarioFactory,
                                                  JogadorFactory,
                                                  PartidaFactory,
                                                  QuadraFactory, TimeFactory)

register(JogadorFactory)
register(TimeFactory)
register(CampeonatoFactory)
register(QuadraFactory)
register(HorarioFactory)
register(PartidaFactory)


@pytest.fixture
def client_autenticado(django_user_model):
    client = APIClient()
    email = "test@test.com"
    password = f'{config("DJANGO_ADMIN_PASSWORD")}'
    user = django_user_model.objects.create_user(
        password=password, email=email
    )
    client.force_authenticate(user)

    return client
