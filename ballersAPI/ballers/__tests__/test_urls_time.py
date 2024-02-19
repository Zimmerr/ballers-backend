import pytest
from rest_framework import status

from ballersAPI.ballers.models.time import Time


@pytest.mark.django_db
def test_url_get_all_times(
    client_autenticado, time_factory
):
    client = client_autenticado
    size = 11

    time_factory.create_batch(size=size)

    response = client.get("/times/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == size


@pytest.mark.django_db
def test_url_get_time(
    client_autenticado, time_factory
):
    client = client_autenticado

    x = time_factory.create(nome='Palmeiras')

    print(x.jogadores.all())

    response = client.get(f'/times/{x.uuid}/')

    assert response.status_code == status.HTTP_200_OK
    assert response.json()['nome'] == "Palmeiras"


@pytest.mark.django_db
def test_url_post_time(
    client_autenticado, jogador_factory
):
    client = client_autenticado

    jogadores = jogador_factory.create_batch(size=5)

    jogadores_payload = [jogador.uuid for jogador in jogadores]

    payload = {
        "nome": "Palmeiras",
        "abreviacao": "SEP",
        "apelido": "Verdão",
        "jogadores": jogadores_payload
    }

    response = client.post('/times/', payload)

    print(payload)
    print(vars(response))

    assert response.status_code == status.HTTP_201_CREATED
    assert Time.objects.count() == 1


@pytest.mark.django_db
def test_url_put_jogador(
    client_autenticado, time_factory, jogador_factory
):
    client = client_autenticado

    x = time_factory.create(nome='Ponte Preta')

    jogadores = jogador_factory.create_batch(size=10)

    jogadores_payload = [jogador.uuid for jogador in jogadores]

    payload = {
        "nome": "S.E. Palmeiras",
        "abreviacao": "SEP",
        "apelido": "Verdão",
        "jogadores": jogadores_payload
    }

    response = client.put(f'/times/{x.uuid}/', payload)

    assert response.status_code == status.HTTP_200_OK
    assert Time.objects.get(nome="S.E. Palmeiras")
