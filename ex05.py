from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int
    funcionario: bool = False


def preço(pessoa: Pessoa, valor: int) -> str:
    match pessoa:
        case Pessoa('Python'):
            return f'Liberado para assistir o filmes de Python!'
        
        case Pessoa(nome, idade) if idade >= 18:
            return f'{nome.capitalize()} paga meia {valor/2}'

        case Pessoa(nome, _, False):
            return f'{nome.capitalize()} paga meia {valor/3}'

print(preço(
    Pessoa('Python', 15, True), 20
))