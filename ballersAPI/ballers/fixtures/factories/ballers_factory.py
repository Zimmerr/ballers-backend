from factory import DjangoModelFactory, Sequence, post_generation
from faker import Faker

from ballersAPI.ballers.models.campeonato import Campeonato
from ballersAPI.ballers.models.jogador import Jogador
from ballersAPI.ballers.models.quadras import Horario, Quadra
from ballersAPI.ballers.models.time import Time

fake = Faker("pt_BR")


class JogadorFactory(DjangoModelFactory):
    class Meta:
        model = Jogador

    nome = Sequence(lambda n: f"{fake.unique.name()}")
    data_nasc = Sequence(lambda n: fake.date(pattern="%Y-%m-%d"))
    cpf = Sequence(lambda n: fake.unique.cpf().replace(".", "").replace("-", ""))
    altura = Sequence(lambda n: fake.unique.random_int(min=0, max=999))


class TimeFactory(DjangoModelFactory):
    class Meta:
        model = Time

    nome = Sequence(lambda n: f"{fake.unique.name()}")
    abreviacao = Sequence(lambda n: fake.unique.pystr(min_chars=3, max_chars=3).upper())
    apelido = Sequence(lambda n: f"{fake.unique.name()} F.C.")

    @post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            return

        if not extracted:
            self.jogadores.set(JogadorFactory.create_batch(size=5))
        else:
            self.jogadores.add(*extracted)


class CampeonatoFactory(DjangoModelFactory):
    class Meta:
        model = Campeonato

    nome = Sequence(lambda n: f"{fake.unique.name()}")
    descricao = Sequence(lambda n: fake.unique.pystr(min_chars=1, max_chars=1000))

    @post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            return

        if not extracted:
            self.times.set(TimeFactory.create_batch(size=5))
        else:
            self.times.add(*extracted)


class QuadraFactory(DjangoModelFactory):
    class Meta:
        model = Quadra

    nome = Sequence(lambda n: f"{fake.unique.name()}")


class HorarioFactory(DjangoModelFactory):
    class Meta:
        model = Horario

    hora = Sequence(lambda n: f"{fake.time()}")
