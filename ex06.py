class Pessoa:
    __match_args__ = 'nome', 'idade', 'funcionaria'

    def __init__(self, nome, idade, funcionario=False):
        self.nome = nome
        self.idade = idade
        self.funcionario = funcionario

    def __repr__(self):
        return self.nome


def preço(pessoas: list[Pessoa]):
    match pessoas:
        case [
            Pessoa('Python', python_idade) as Python,
            Pessoa('Pypi', pypi_idade) as Pypi
        ]:
            return Python, python_idade, Pypi, pypi_idade

        case [(Pessoa('Pypi') | Pessoa('Python') as pessoa)]:
            return pessoa
        

print(preço(
    [Pessoa('Pypi', 18, True), Pessoa('Python', 18, True)]
))
