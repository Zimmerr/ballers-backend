import pytest
from rest_framework import status

from ballersAPI.ballers.models.campeonato import Campeonato


@pytest.mark.django_db
def test_url_get_all_campeonatos(
    client_autenticado, campeonato_factory
):
    client = client_autenticado
    size = 11

    campeonato_factory.create_batch(size=size)

    response = client.get("/campeonatos/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == size


@pytest.mark.django_db
def test_url_get_campeonato(
    client_autenticado, campeonato_factory
):
    client = client_autenticado

    x = campeonato_factory.create(nome='Brasileirao')

    response = client.get(f'/campeonatos/{x.uuid}/')

    assert response.status_code == status.HTTP_200_OK
    assert response.json()['nome'] == "Brasileirao"


@pytest.mark.django_db
def test_url_post_campeonato(
    client_autenticado, time_factory
):
    client = client_autenticado

    times = time_factory.create_batch(size=8)

    times_payload = [time.uuid for time in times]

    payload = {
        "nome": "Palmeiras",
        "descricao": """O Campeonato Brasileiro de Futebol, também conhecido como Campeonato Brasileiro,
                        Brasileirão e Série A, é a liga brasileira de futebol profissional entre clubes do Brasil,
                        sendo a principal competição futebolística no país.""",
        "times": times_payload
    }

    response = client.post('/campeonatos/', payload)

    assert response.status_code == status.HTTP_201_CREATED
    assert Campeonato.objects.count() == 1


@pytest.mark.django_db
def test_url_put_jogador(
    client_autenticado, campeonato_factory, time_factory
):
    client = client_autenticado

    x = campeonato_factory.create(nome='Brasileirão')

    times = time_factory.create_batch(size=10)

    times_payload = [time.uuid for time in times]

    payload = {
        "nome": "Brasileirão 2024",
        "descricao": """O Campeonato Brasileiro de Futebol, também conhecido como Campeonato Brasileiro,
                        Brasileirão e Série A, é a liga brasileira de futebol profissional entre clubes do Brasil,
                        sendo a principal competição futebolística no país.""",
        "times": times_payload
    }

    response = client.put(f'/campeonatos/{x.uuid}/', payload)

    assert response.status_code == status.HTTP_200_OK
    assert Campeonato.objects.get(nome="Brasileirão 2024")
