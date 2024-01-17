import pytest
from rest_framework import status

from ballersAPI.ballers.models.jogador import Jogador


@pytest.mark.django_db
def test_url_get_all_jogadores(
    client_autenticado, jogador_factory
):
    client = client_autenticado
    size = 11

    jogador_factory.create_batch(size=size)

    response = client.get("/jogadores/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == size


@pytest.mark.django_db
def test_url_get_jogador(
    client_autenticado, jogador_factory
):
    client = client_autenticado

    x = jogador_factory.create(nome='Roberto')

    response = client.get(f'/jogadores/{x.id}/')

    assert response.status_code == status.HTTP_200_OK
    assert response.json()['nome'] == "Roberto"


@pytest.mark.django_db
def test_url_post_jogador(
    client_autenticado
):
    client = client_autenticado

    payload = {
        "nome": "Roberto da Silva",
        "cpf": "12345678910",
        "data_nasc": "1999-01-01",
        "altura": 175
    }

    response = client.post('/jogadores/', payload)

    assert response.status_code == status.HTTP_201_CREATED
    assert Jogador.objects.count() == 1


@pytest.mark.django_db
def test_url_put_jogador(
    client_autenticado, jogador_factory
):
    client = client_autenticado

    x = jogador_factory.create(nome='Roberto')

    payload = {
        "nome": "Roberto da Silva",
        "cpf": "12345678910",
        "data_nasc": "1999-01-01",
        "altura": 175
    }

    response = client.put(f'/jogadores/{x.id}/', payload)

    assert response.status_code == status.HTTP_200_OK
    assert Jogador.objects.get(nome="Roberto da Silva")


@pytest.mark.django_db
def test_url_delete_jogador(
    client_autenticado, jogador_factory
):
    client = client_autenticado

    x = jogador_factory.create(nome='Roberto')

    response = client.delete(f'/jogadores/{x.id}/')

    assert response.status_code == status.HTTP_200_OK
    assert Jogador.objects.count() == 1
    assert Jogador.objects.get(id=x.id).ativo is False
