# Generated by Django 5.0.1 on 2024-02-16 14:45

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ballers", "0002_jogador_ativo_alter_jogador_data_nasc"),
    ]

    operations = [
        migrations.CreateModel(
            name="Time",
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
                ("abreviacao", models.CharField(max_length=3, verbose_name="Nome")),
                ("apelido", models.CharField(max_length=30, verbose_name="Nome")),
                ("jogadores", models.ManyToManyField(to="ballers.jogador")),
            ],
            options={
                "verbose_name": "Time",
                "verbose_name_plural": "Times",
            },
        ),
    ]