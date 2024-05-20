"""
Algoritmos gulosos:

-> como lidar com o impossível: problemas que não tem um algoritmo de solução
rápida (problemas NP-completo(não polinomiais))
-> Como identificar pesses problemas ao se deparar com eles, de forma que não
perca tempo tentando achar um algoritmo rápido para solcioná-los.
-> Conhecerá os algoritmos de aproximação, que podem ser usados para encontrar,
de maneira rápida, uma solução aproximada para um problema NP-completo.
-> Conhecerá a estratégia gulosa, uma estratégia muito simples para resolver
problemas.
"""

"""
Algoritmo de aproximação:
- Quando é necessário muito tempo para calcular a solução exata, um algoritmo
de aproximação é uma boa ideia e funciona
São analisados:
- Por sua rapidez;
- Pela capacidade de chegar à solução ideal.

Nesta situação de ter uma estação de rádio em cada um dos 50 estados:
Pegar a estação que abrange o maior número de estados que ainda não foram
cobertos. Tudo bem se a estação abranger alguns estados que já foram cobertos.
Repetir até que todos os estados tenham sido cobertos.
"""

estados_abranger = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

estacoes = {}
estacoes['kum'] = set(['id', 'nv', 'ut'])
estacoes['kdois'] = set(['id', 'wa', 'mt'])
estacoes['ktres'] = set(['or', 'nv', 'ca'])
estacoes['kquatro'] = set(['nv', 'ut'])
estacoes['kcinco'] = set(['ca', 'az'])
# print(estacoes.items())
estacoes_final = set('')

while estados_abranger:
    melhor_estacao = None
    estados_cobertos = set('')

    for estacao, estados_por_estacao in estacoes.items():
        cobertos = estados_abranger & estados_por_estacao
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos

            estados_abranger -= estados_cobertos
            estacoes_final.add(melhor_estacao)

print(estacoes_final)
