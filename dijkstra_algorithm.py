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
print(grafo)

infinito = float('inf')
custos: dict = {}
custos['a'] = 6
custos['b'] = 2
custos['fim'] = infinito

pais: dict = {}
pais['a'] = 'inicio'
pais['b'] = 'inicio'
pais['fim'] = None

processados: list = []

"""
enquanto houver grafos a serem processados...
while processados is not None:
pegue o vértice que está mais proximo do início...

atualize os custos para seus vizinhos...
se qualquer um dos custos dos vizinhos for atualizado, atualize tb o pai...
marque o vértice como processado...
repita
"""

# encontra o custo mais baixo que ainda não foi processado


def ache_no_custo_mais_baixo(custos):
    ...


nodo = ache_no_custo_mais_baixo(custos)
# caso todos os vértices tenham sido processados, finaliza
while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    # percorre todos os vértices
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        # caso seja mais barato chegar a um vizinho a partir desse vértice...
        if custos[n] > novo_custo:
            # atualiza seu custo
            custos[n] = novo_custo
            # este vertice se torna o novo pai para o vizinho
            pais[n] = nodo
    # marca o vertice como processado, adicionando-o a lista processados
    processados.append(nodo)
    # encontra o próximo vértice a ser processado e o algoritmo é repetido.
    nodo = ache_no_custo_mais_baixo(custos)
