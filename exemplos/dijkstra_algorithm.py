grafo: dict = {}
grafo['inicio'] = {}
grafo['inicio']['a'] = 5
grafo['inicio']['b'] = 2
grafo['a'] = {}
grafo['a']['c'] = 4
grafo['a']['d'] = 2
grafo['b'] = {}
grafo['b']['a'] = 8
grafo['b']['d'] = 7
grafo['c'] = {}
grafo['c']['d'] = 6
grafo['c']['fim'] = 3
grafo['d'] = {}
grafo['d']['fim'] = 1
grafo['fim'] = {}
print('grafo ', grafo)

infinito = float('inf')
custos: dict = {}
custos['a'] = 5
custos['b'] = 2
custos['c'] = infinito
custos['d'] = infinito
custos['fim'] = infinito
print('custos ', custos)

pais: dict = {}
pais['a'] = 'inicio'
pais['b'] = 'inicio'
pais['c'] = 'a'
pais['d'] = 'a', 'b', 'c'
pais['fim'] = None
print('pais ', pais)

processados: list = []
print('processados ', processados)


print('\n#########################\n')


# encontra o custo mais baixo que ainda não foi processado
def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float('inf')
    vertice_custo_mais_baixo = None
    for vertice in custos:
        custo = custos[vertice]
        if custo < custo_mais_baixo and vertice not in processados:
            custo_mais_baixo = custo
            vertice_custo_mais_baixo = vertice
    if vertice_custo_mais_baixo is not None and custo_mais_baixo <= custo:
        print(f'vertice {vertice_custo_mais_baixo}, custo {custo_mais_baixo}')
    return vertice_custo_mais_baixo


vertice = ache_no_custo_mais_baixo(custos)
# caso todos os vértices tenham sido processados, finaliza
ciclo = 1
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
            print(f'custo dos vizinhos: {vizinhos[n]}')
    # marca o vertice como processado, adicionando-o a lista processados
    processados.append(vertice)
    if len(processados) < len(custos):
        print(f'analisados: {processados}')
    if 'fim' not in processados:
        print(f'ciclo: {ciclo}°\n')
    ciclo += 1
    # encontra o próximo vértice a ser processado e o algoritmo é repetido.
    vertice = ache_no_custo_mais_baixo(custos)


ache_no_custo_mais_baixo(custos)
