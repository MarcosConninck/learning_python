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


fila_de_pesquisa: deque = deque()
fila_de_pesquisa += grafo["eu"]


def pessoa_vendedora(pessoa):
    if pessoa == "anuj":
        return True  # sim! pronto
    else:
        return False  # não! adiciona os vizinhos dela a fila


while fila_de_pesquisa:  # enquanto a fila não estiver vazia
    pessoa = fila_de_pesquisa.popleft()  # pega primeira pessoa da fila
    if pessoa_vendedora(pessoa) is True:  # conferindo se a pessoa é vendedora
        print(f'{pessoa} é vendedor de manga')
        break
    elif fila_de_pesquisa == deque([]):
        print("não há vendedores de manga")
    else:
        fila_de_pesquisa += grafo[pessoa]  # chama o loop novamente
