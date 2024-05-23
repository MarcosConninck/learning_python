"""
Nesta sessão irei trazer conceitos, além do algoritmo em si:
    Classificação (separar em grupos) e regressão(adivinhar uma resposta).
    Sistema de recomendações de filmes
    Extrair e escolher uma boa característica (converter um ítem em uma lista
        de números que podem ser comparados)
    Introdução ao aprendizado de máquina


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

###############################################################################

"""
    Criando sistema de recomendações.

Suponha usuários de um sistema de streaming e você precisa classificá-los.
Eles são agrupados por similaridades, gostos similares são colocados próximos
uns dos outros.

Similar ao problema das laranjas vs toranjas, um usuário próximo a diversos
outros usuários que têm o mesmo gosto... ao recomendar um filme, provavelmente
ele também irá gostar, certo? mas como fazer para descobrir a distância entre
eles?

###############################################################################

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
nomes = ('jose', 'rafael', 'marcos')


def distancia_conjuntos(conjunto_a, conjunto_b):
    i = 0
    distancia = 0

    for _ in conjunto_a:
        distancia += (conjunto_a[i] - conjunto_b[i])**2
        i += 1

    print(f'distancia: "{distancia}"')
    return distancia


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

###############################################################################

    Regressão

Tenta adivinhar qual valor virá.
Recebemos aqui diversas avaliações de um filme:
"""

valores = (5, 4, 4, 5, 3)


def calcula_media(valores):
    qtd_valores = len(valores)
    soma = 0
    for n in valores:
        soma += n
    media = soma / qtd_valores
    print(f'media = {media}')  # 4.2


calcula_media(valores)
"""
Essa média pode ser usada para tentar medir a valiação do filme.
Isto é chamado de regressão

duas coisas que K-vizinhos precisa:
Classificação = classificar em grupos
Regressão = adivinhar uma resposta (como um número)

A regressão é muito útil.
Por exemplo, tentar prever a quantidade de vendas de pão em uma padaria,
existe um conjunto de caracteristicas sobre este problema:

-> o Clima em uma escala de 1 - 5
-> Fim de semana ou feriado? 1 - sim, 0 - não
-> Há Jogo no dia? 1 - sim, 0 - não

Além disto, você sabe quantos pães vendeu anteriormente para cada conjunto de
caracteristicas:
"""
a = (5, 1, 0)  # 300
b = (3, 1, 1)  # 225
c = (1, 1, 0)  # 75
d = (4, 0, 1)  # 200
e = (4, 0, 0)  # 150
f = (2, 0, 0)  # 50

# clima bom, é fim de semana, sem jogo
x = (4, 1, 0)

total_valores = (
    distancia_conjuntos(a, x),  # 1 mais proximo de x
    distancia_conjuntos(b, x),  # 2 mais proximo de x
    distancia_conjuntos(c, x),  # 9
    distancia_conjuntos(d, x),  # 2 mais proximo de x
    distancia_conjuntos(e, x),  # 1 mais proximo de x
    distancia_conjuntos(f, x),  # 5
)

# A partir daqui, vamos utilizar a quantidade de pão vendido das distancias
# mais próximas de x, sendo elas: a, b, d, e

paes_vendidos = (300, 225, 200, 150)
calcula_media(paes_vendidos)  # 218.75

###############################################################################
"""
    Similaridade do Cosseno

Até o momento utilizamos a formula de pitágoras para medir a distância entre os
conjuntos, mas se tivessemos dois usuários que avaliassem o mesmo filme com
notas 4 e 5, sendo que eles têm o gosto muito similar, mas o primeiro usuário é
mais conservador em dar nota. Dependendo da medição da distância, eles poderiam
não entrar no mesmo grupo para sugestão de filmes.
Diferente da formula da medição da distância, a similaridade do cosseno não
mede a distância entre dois vetores, mas sim compara o ângulo entre eles,
sendo assim, ela lida melhor com os exemplos apresentados até agora.
"""
###############################################################################

"""
    Escolhendo boas Características

Ao trabalhar com o algoritmo dos k-vizinhos mais próximos, é muito importante
escolher as características certas a serem comparadas, que são:
-> Diretamente correlacionadas ao que você está tentando recomendar
-> Imparciais (se as únicas opções fornecidas aos usuários forem filmes de
comédia, esta avaliação não fornecerá nenhuma informação útil sobre o gosto
dos usuários em relação a filmes de ação, por ex)

Uma outra boa dica para escolha da quantidade de vizinhos é:
Se você possui N usuários, para classificação, tenha pelo menos raiz(N)
vizinhos
"""
###############################################################################

"""
    Introdução ao aprendizado de máquina

O algoritmo dos k-vizinhos mais próximos é muito útil e é a introdução ao ML.

OCR (optical character recognition)
Com ele é possível fotografar um texto e digitalizar as palavras(não em imagem)
Como reconhecer a imagem de um número?
Para fazer isso ele segue estes passos:
-> percorra diversas imagens de números e extraia características de cada um
deles (treinamento)
-> quando obtiver uma nova imagem, extraia as caracteristicas dessa imagem e
veja quais são os vizinhos mais próximos

Este é um problema similar à classificação de laranjas e toranjas, apresentado
logo no início, mas de um modo geral, algoritmos OCR medem linhas, pontos e
curvas.
Portanto, se você recebe um novo caractere, é possivel extrair suas
caracteristicas.

    Criando um filtro de SPAM

Os filtros de spam utilizam outro algoritmo simples, o classificador Naive
Bayes, com alguns dados.

Por exemplo:
atualize a senha        -> não é spam
você ganhou na loteria! -> spam
me envie sua senha      -> spam
você é o visitante 1000 -> spam
feliz aniversário       -> não é spam

    Prevendo a Bolsa de Valores

É uma tarefa bem difícil prever se as ações da bolsa vão subir ou descer.
Como extraímos boas características?
Imagine que você tenha estipulado que se as ações subiram ontem, elas subirão
hoje, é uma boa? Prever o futuro é dificl com tantas variáveis envolvidas.

"""
