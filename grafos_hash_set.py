"""
Tabelas Hash possuem chave->valor associados.
São muito mais rápidas que o tipo list
uma chave deve estar associada a apenas um valor
"""
from collections import deque

# exercicio utilizando hash:
votaram: dict = {}


def verifica_eleitor(nome: str) -> None:
    if votaram.get(nome):
        print("Já votou!")
    else:
        votaram[nome] = True
        print("Pode votar")


# verifica_eleitor('Marcos')
# verifica_eleitor('Angelica')
# verifica_eleitor('Angelica')
# print(votaram)

# Algoritmo de pesquisa em largura e grafos:
# Exercicio de grafos, encontrando vendedor de manga:

grafo: dict = {}

grafo["eu"] = ["bob", "claire", "alice"]
grafo["bob"] = ["anuj", "peggy"]
grafo["claire"] = ["tom", "jonny"]
grafo["alice"] = ["peggy"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["tom"] = []
grafo["jonny"] = []

# 1º criar uma fila contendo todas as pessoas a serem verificadas
# 2º retire uma pessoa da fila
# 3º confira se a pessoa é um vendedor de manga (if)
# 4º sim! pronto | não! adicionar os vizinhos dela a fila
# 5º chama função novamente
# 6º caso a fila esteja vazia, não há vendedores


def pessoa_vendedora(pessoa: str) -> bool:
    if pessoa == vendedor:
        return True  # sim! pronto
    return False  # não! adiciona os vizinhos dela a fila


def pesquisa(nome: str) -> bool:
    print('Pessoas na lista:')
    for n in grafo:
        print(f'-> {n}')
    fila_de_pesquisa: deque = deque()
    fila_de_pesquisa += grafo[nome]
    # Mantêm as pessoas verificadas em uma lista, para não entrar em loop inf
    verificadas = []
    # enquanto a fila não estiver vazia
    while fila_de_pesquisa:
        # pega primeira pessoa da fila
        pessoa = fila_de_pesquisa.popleft()
        print(f'verificando: {pessoa}')
        if pessoa not in verificadas:
            # conferindo se a pessoa é vendedora
            if pessoa_vendedora(pessoa) is True:
                print(f'{pessoa} é vendedor de manga')
                return True
            # chama o loop novamente
            else:
                # adiciona em ordem novas pessoas a serem verificadas
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)

        elif fila_de_pesquisa == deque([]):
            print("não há vendedores de manga, todos foram verificados")

    return False


print(grafo)
vendedor = input('Determine o nome do vendedor: ').lower()
pesquisa('eu')
