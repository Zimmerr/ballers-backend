import pytest
from rest_framework import status

from ballersAPI.ballers.models.partida import Partida


@pytest.mark.django_db
def test_url_get_all_partidas(
    client_autenticado, partida_factory
):
    client = client_autenticado
    size = 11

    partida_factory.create_batch(size=size)

    response = client.get("/partidas/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == size


@pytest.mark.django_db
def test_url_get_partida(
    client_autenticado, partida_factory
):
    client = client_autenticado

    x = partida_factory.create(data="2022-12-12")

    response = client.get(f'/partidas/{x.uuid}/')

    assert response.status_code == status.HTTP_200_OK
    assert response.json()['data'] == "2022-12-12"


@pytest.mark.django_db
def test_url_post_partida(
    client_autenticado, time_factory,
    campeonato_factory, horario_factory,
    quadra_factory
):
    client = client_autenticado

    time_1 = time_factory.create()
    time_2 = time_factory.create()
    campeonato = campeonato_factory.create()
    horario = horario_factory.create()
    quadra = quadra_factory.create()

    payload = {
        "time_casa": time_1.uuid,
        "time_fora": time_2.uuid,
        "campeonato": campeonato.uuid,
        "horario": horario.uuid,
        "quadra": quadra.uuid,
        "data": "2024-01-01",
    }

    response = client.post('/partidas/', payload)

    assert response.status_code == status.HTTP_201_CREATED
    assert Partida.objects.count() == 1

    response = client.post('/partidas/', payload)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert Partida.objects.count() == 1

    payload["data"] = '2024-01-02'

    response = client.post('/partidas/', payload)

    assert response.status_code == status.HTTP_201_CREATED
    assert Partida.objects.count() == 2


@pytest.mark.django_db
def test_url_put_partida(
    client_autenticado, time_factory,
    campeonato_factory, horario_factory,
    quadra_factory, partida_factory
):
    client = client_autenticado

    x = partida_factory.create(data='2020-01-01')

    time_1 = time_factory.create()
    time_2 = time_factory.create()
    campeonato = campeonato_factory.create()
    horario = horario_factory.create()
    quadra = quadra_factory.create()

    payload = {
        "time_casa": time_1.uuid,
        "time_fora": time_2.uuid,
        "campeonato": campeonato.uuid,
        "horario": horario.uuid,
        "quadra": quadra.uuid,
        "data": "2024-03-03",
    }

    response = client.put(f'/partidas/{x.uuid}/', payload)

    assert response.status_code == status.HTTP_200_OK
    assert Partida.objects.get(data="2024-03-03")


@pytest.mark.django_db
def test_url_delete_partida(
    client_autenticado, partida_factory
):
    client = client_autenticado

    x = partida_factory.create()

    assert Partida.objects.count() == 1

    response = client.delete(f'/partidas/{x.uuid}/')

    assert response.status_code == status.HTTP_200_OK
    assert Partida.objects.count() == 0


@pytest.mark.django_db
def test_url_delete_partida_finalizada(
    client_autenticado, partida_factory
):
    client = client_autenticado

    x = partida_factory.create(finalizada=True)

    assert Partida.objects.count() == 1

    response = client.delete(f'/partidas/{x.uuid}/')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert Partida.objects.count() == 1
