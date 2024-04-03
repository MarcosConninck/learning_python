# incompleto, revisar

"""
Este projeto foi desenvolvido para encontrar um nome em uma lista, utilizando
o algoritmo de busca binária em uma lista relativamente grande, podendo ser
aplicado a listas muito maiores, com a eficiência de busca O(log n) em relação
a busca item a item, que seria O(n), o que consumiria muito mais tempo.

Ao invez de realizar a busca 100 vezes (pior cenário), este algoritmo encontra
o item buscado em até log 2 100 tentativas (7 tentativas). Além disto, quanto
mais itens na lista, maior é a diferença da eficiencia dos dois métodos de
busca.
"""

# 1º Passo foi pegar o <tbody> do site, que contém a lista.
# 2º Passo extrair os dados da lista html
# 3º Tratar os dados, formatação, acentuação, etc
# 4º Utilizar o algoritmo de pesquisa binária (cap 01 do livro)

# Falta melhorar algumas coisas no código, como por ex.:
# criar interface gráfica com PySide6

from bs4 import BeautifulSoup
from itertools import chain
from unidecode import unidecode

# primeiro inserir o html
caminho_html = 'exemplos\\html_lista.html'
with open(caminho_html, "r") as f:
    html_string = f.read()

# extraindo a soup
soup = BeautifulSoup(html_string, 'html.parser')
# nova lista onde será adicionado o conteudo da soup
dados_tabela = []
# encontrando todas as tags <tr>
tabela = soup.find_all('tr')
for linha in tabela:
    dados_linha = [coluna.text.strip()
                   for coluna in linha.find_all(['td', 'th'])]
    # usando list comprehencion
    dados_tabela.append(dados_linha)
    # juntando às listas de listas

# removendo o título das colunas
dados_tabela.remove(dados_tabela[0])

# removendo numeradores das linhas de cada lista
for dado in dados_tabela:
    dado.remove(dado[0])


# Algorítmo de pesquisa binária adaptado à lista
def pesquisa_binaria(lista: list, nome_alvo: str):
    tentativa = 0
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        tentativa = tentativa + 1
        print(f'tentativa = {tentativa}')
        alvo = lista[meio]
        if alvo == nome_alvo:
            print(f'nome encontrado... "{alvo}"'
                  f'em {tentativa} tentativas, o nome está entre os 100')
            return meio
        if alvo > nome_alvo:
            alto = meio - 1
        else:
            baixo = meio + 1
    # se o ítem é inexistente:
    print("nome não está está entre os 100")
    return None


def processar_entrada(texto: str):
    texto_processado = unidecode(texto).lower()
    return texto_processado


def processar_lista(lista: list):
    lista_unidecoded = []
    for item in lista:
        item_processado = unidecode(item).lower()
        lista_unidecoded.append(item_processado)
    return lista_unidecoded


# juntando todas as listas em uma
lista_completa = list(chain.from_iterable(dados_tabela))

# lista em ordem alfabética
lista_ordenada = sorted(lista_completa)

# lista sem upper e sem acentuação
lista_unidecoded = (processar_lista(lista_ordenada))


def print_lista_ordenada():
    for item in lista_ordenada:
        print(item)


frase1 = 'Digite o nome a ser buscado na lista, para saber se está entre os \
100 nomes mais populares para bebês de 2024 \n'

nome_procurar = input(frase1)
# tratando input do usuário:
nome_procurar_tratado = processar_entrada(nome_procurar)


pesquisa_binaria(lista_unidecoded, nome_procurar_tratado)
