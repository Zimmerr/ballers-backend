# Generated by Django 4.2.7 on 2024-01-15 15:40

import uuid

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Jogador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "criado_em",
                    models.DateTimeField(auto_now_add=True, verbose_name="Criado em"),
                ),
                (
                    "alterado_em",
                    models.DateTimeField(auto_now=True, verbose_name="Alterado em"),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("nome", models.CharField(max_length=150, verbose_name="Nome")),
                ("altura", models.IntegerField(verbose_name="Altura (em cm)")),
                ("data_nasc", models.DateField()),
                (
                    "cpf",
                    models.CharField(
                        max_length=11,
                        unique=True,
                        validators=[django.core.validators.MinLengthValidator(11)],
                    ),
                ),
            ],
            options={
                "verbose_name": "Jogador",
                "verbose_name_plural": "Jogadores",
            },
        ),
    ]
