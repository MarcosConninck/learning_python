"""
Este algorimo, em específico, é similar a pesquisa em largura, porém leva em
conta o "peso" de cada trajeto, de forma ponderada.

O algoritmo possui 4 etapas:
    -> Encontre o vertice mais "barato". Este é o vértice em que você consegue
    chegar no menor tempo possível.
    -> Atualize o custo dos vizinhos deste vértice.
    -> Repita até que você tenha feito isso para cada vértice do grafo. (loop)
    -> Calcule o caminho final
"""
grafo: dict = {}
grafo['inicio'] = {}
grafo['inicio']['a'] = 6
grafo['inicio']['b'] = 2
grafo['a'] = {}
grafo['a']['fim'] = 1
grafo['b'] = {}
grafo['b']['a'] = 3
grafo['b']['fim'] = 5
grafo['fim'] = {}
print('grafo ', grafo)

infinito = float('inf')
custos: dict = {}
custos['a'] = 6
custos['b'] = 2
custos['fim'] = infinito
print('custos ', custos)

pais: dict = {}
pais['a'] = 'inicio'
pais['b'] = 'inicio'
pais['fim'] = None
print('pais ', pais)

processados: list = []
print('processados ', processados)

"""
enquanto houver grafos a serem processados...
while processados is not None:
pegue o vértice que está mais proximo do início...
atualize os custos para seus vizinhos...
se qualquer um dos custos dos vizinhos for atualizado, atualize tb o pai...
marque o vértice como processado...
repita
"""

print('\n#########################\n')


def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float('inf')
    vertice_custo_mais_baixo = None
    for vertice in custos:
        custo = custos[vertice]
        if custo < custo_mais_baixo and vertice not in processados:
            custo_mais_baixo = custo
            vertice_custo_mais_baixo = vertice
    if vertice_custo_mais_baixo is not None:
        print(f'vertice analisado: {
              vertice_custo_mais_baixo}, custo {custo_mais_baixo}')
    return vertice_custo_mais_baixo


vertice = ache_no_custo_mais_baixo(custos)
# caso todos os vértices tenham sido processados, finaliza
while vertice is not None:
    custo = custos[vertice]
    vizinhos = grafo[vertice]
    # percorre todos os vértices
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        # caso seja mais barato chegar a um vizinho a partir desse vértice...
        if custos[n] > novo_custo:
            # atualiza seu custo
            custos[n] = novo_custo
            # este vertice se torna o novo pai para o vizinho
            pais[n] = vertice
    # marca o vertice como processado, adicionando-o a lista processados
    processados.append(vertice)
    # encontra o próximo vértice a ser processado e o algoritmo é repetido.
    vertice = ache_no_custo_mais_baixo(custos)


ache_no_custo_mais_baixo(custos)
