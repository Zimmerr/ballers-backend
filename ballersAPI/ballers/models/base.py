import uuid

from django.db import models


class CriadoEm(models.Model):
    criado_em = models.DateTimeField("Criado em", editable=False, auto_now_add=True)

    class Meta:
        abstract = True


class TemAlteradoEm(models.Model):
    alterado_em = models.DateTimeField("Alterado em", editable=False, auto_now=True)

    class Meta:
        abstract = True


class TemUUID(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @classmethod
    def by_uuid(cls, uuid):
        return cls.objects.get(uuid=uuid)

    class Meta:
        abstract = True


class Ativavel(models.Model):
    ativo = models.BooleanField("Está ativo?", default=True)

    class Meta:
        abstract = True


class ModeloBase(TemUUID, CriadoEm, TemAlteradoEm):
    class Meta:
        abstract = True
