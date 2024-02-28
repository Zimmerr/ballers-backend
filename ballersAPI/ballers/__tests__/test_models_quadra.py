import datetime

import pytest

from ballersAPI.ballers.models.quadras import Horario, Quadra


@pytest.mark.django_db
def test_model_get_all_quadras(
    quadra_factory
):

    size = 11
    quadra_factory.create_batch(size=size)

    quadras = Quadra.objects.all()

    assert len(quadras) == size


@pytest.mark.django_db
def test_model_get_quadra(
    quadra_factory
):
    nome = 'Quadra Grande'
    quadra_factory.create(nome=nome)

    quadra = Quadra.objects.get(nome=nome)

    assert quadra
    assert quadra.nome == nome


@pytest.mark.django_db
def test_model_create_quadra():
    nome = 'Quadra Média'
    quadra = Quadra.objects.create(nome=nome)

    assert quadra
    assert quadra.nome == nome


@pytest.mark.django_db
def test_model_update_quadra(quadra_factory):
    quadra_factory.create()
    novo_nome = 'Quadra Pequena'

    quadra = Quadra.objects.first()

    quadra.nome = novo_nome
    quadra.save()

    quadra_nova = Quadra.objects.get(nome=novo_nome)

    assert quadra_nova
    assert quadra_nova.nome == novo_nome


@pytest.mark.django_db
def test_model_delete_quadra(quadra_factory):
    size = 5
    quadra_factory.create_batch(size=size)

    Quadra.objects.last().delete()

    assert Quadra.objects.all().count() == (size-1)


@pytest.mark.django_db
def test_model_get_all_horarios(
    horario_factory
):

    size = 11
    horario_factory.create_batch(size=size)

    horarios = Horario.objects.all()

    assert len(horarios) == size


@pytest.mark.django_db
def test_model_get_horario(
    horario_factory
):
    hora = datetime.time(hour=18, minute=59)
    horario_factory.create(hora=hora)

    horario = Horario.objects.get(hora=hora)

    assert horario
    assert horario.hora == hora


@pytest.mark.django_db
def test_model_create_horario():
    hora = datetime.time(hour=8, minute=15)
    horario = Horario.objects.create(hora=hora)

    assert horario
    assert horario.hora == hora


@pytest.mark.django_db
def test_model_update_horario(horario_factory):
    horario_factory.create()
    nova_hora = datetime.time(hour=12, minute=1)

    horario = Horario.objects.first()

    horario.hora = nova_hora
    horario.save()

    horario_nova = Horario.objects.get(hora=nova_hora)

    assert horario_nova
    assert horario_nova.hora == nova_hora


@pytest.mark.django_db
def test_model_delete_horario(horario_factory):
    size = 5
    horario_factory.create_batch(size=size)

    Horario.objects.last().delete()

    assert Horario.objects.all().count() == (size-1)
