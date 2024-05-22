"""
K-Vizinhos mais proximos.

Classificando laranja vs toranjas:
grafico = tamanho * cor
onde:
pequeno < grande
laranja < vermelho

quanto maior e mais vermelho = toranja
quanto menor e mais laranja  = laranja

mas e se tiver a fruta 'x' no meio desta classificação?
ai que entra em ação k-vizinhos mais proximos...
digamos que se tenha 2 laranjas próximas ao x, mas apenas 1 toranja próxima,
provavelmente 'x' é laranja
"""

#################################################################
"""
 criando sistema de recomendações

descobrindo a distância de duas listas:
distancia = ((a1 - b1)**2 + (a2 - b2)**2 ...)**(1/2)
"""

priyanka = (3, 4, 4, 1, 4)
morpheus = (2, 5, 1, 3, 1)


i = 0
distancia = 0
for _ in priyanka:
    distancia += (priyanka[i] - morpheus[i])**2
    i += 1
print(f'raiz da distancia: "{distancia}" = {round(distancia**(1/2), 3)}')

# quando mais alta a distância, mais longe estão
# a comparação com k-vizinhos é descobrir quandos vizinhos possui mais perto
# para classificar como pertencendo a um grupo ou outro

avaliacoes = (5, 4, 4, 5, 3)

i = 0
acumulo_valores = 0
for _ in avaliacoes:
    acumulo_valores += avaliacoes[i]
    i += 1
media = acumulo_valores / len(avaliacoes)
print(f'média das avaliações: {media}')
