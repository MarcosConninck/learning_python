"""
    K-Vizinhos mais proximos.

Classificando laranja vs toranjas:
grafico = tamanho * cor
onde:
pequeno < grande
laranja < vermelho

quanto maior e mais vermelho = toranja
quanto menor e mais laranja  = laranja

Mas e se tiver a fruta 'x' no meio desta classificação?
Ai que entra em ação k-vizinhos mais proximos...
Digamos que se tenha 2 laranjas próximas ao x, mas apenas 1 toranja próxima,
provavelmente 'x' é laranja
"""

#################################################################

"""
    Criando sistema de recomendações.

Suponha usuários de um sistema de streaming e você precisa classificá-los.
Eles são agrupados por similaridades, gostos similares são colocados próximos
uns dos outros.

Similar ao problema das laranjas vs toranjas, um usuário próximo a diversos
outros usuários que têm o mesmo gosto... ao recomendar um filme, provavelmente
ele também irá gostar, certo? mas como fazer para descobrir a distância entre
eles?


    Extração de características:


Primeiramente descobrindo a distância de duas listas utilizando o teorema de
Pirágoras:

distância em um grafico comum de dois eixos x y entre dois pontos é:
distancia_plano_cartesiano = ((a1 - b1)**2 + (a2 - b2)**2)**(1/2)


Jose e Marcos dão "estrelas" para cada estilo de filme de sua preferencia,
sendo [comédia, ação, drama, terror, romance], desta forma, vamos ao código:

distancia = ((a1 - b1)**2 + (a2 - b2)**2 + (a2 - b2)**2 + ...)**(1/2)
um matemático diria que estariamos calculando a distância em um plano de 5
dimensões, mas a fórmula continua a mesma.
"""

jose = (3, 4, 4, 1, 4)
rafael = (4, 3, 5, 1, 5)
marcos = (2, 5, 1, 3, 1)


def distancia_conjuntos(conjunto_a, conjunto_b):
    i = 0
    distancia = 0

    for _ in conjunto_a:
        distancia += (conjunto_a[i] - conjunto_b[i])**2
        i += 1

    print(f'raiz da distancia: "{distancia}" = {round(distancia**(1/2), 3)}')


# distância jose - rafael:
distancia_conjuntos(jose, rafael)  # 2.000
# Jose e Rafael são bem semelhantes, assim, se recomendar filmes para Jose,
# Rafael também vai gostar.


# distância jose - marcos:
distancia_conjuntos(jose, marcos)  # 4.899


"""
Quando maior a distância, mais longe estão.
A comparação com k-vizinhos é descobrir quandos vizinhos possui mais perto
para classificar como pertencendo a um grupo ou outro.


Resumindo, a distância informa a similaridade entre os conjuntos.
"""
