from factory import DjangoModelFactory, Sequence
from faker import Faker

from ballersAPI.ballers.models.jogador import Jogador

fake = Faker("pt_BR")


class JogadorFactory(DjangoModelFactory):
    class Meta:
        model = Jogador

    nome = Sequence(lambda n: f"{fake.unique.name()}")
    data_nasc = Sequence(lambda n: fake.date(pattern="%Y-%m-%d"))
    cpf = Sequence(lambda n: fake.unique.cpf().replace(".", "").replace("-", ""))
    altura = Sequence(lambda n: fake.unique.random_int(min=0, max=999))
