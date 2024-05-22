"""
A programação dinâmica é um método de desenvolvimento que busca encontrar a
solução de vários subproblemas para, daí então, encontrar a solução do problema
geral.
Como, por exemplo, encontrar o termo N da sequência de Fibonacci é um problema
que pode ser resolvido com Programação Dinâmica, dividir para conquistar ou
ainda com recursão (exemplos demonstrados abaixo)

Basicamente a divisão de um problema maior em subproblemas, para mais facil
resolução. Desde que os subproblemas não dependam um do outro.

Util quando se está tentando otimizar em relação a um limite.

Soluções gerais:
-> envolve uma tabela.
-> Valores nas células são, geralemte, o que se esta tentando otimizar.
-> Cada célula é um subproblema, portanto, pense como é possivel dividi-lo em
outros subproblemas, pois isso ajudara a descobrir quais são os seus eixos.
"""

# Sequencia de Fibonacci

# n pertencendo aos números inteiros
# n é a é o valor do número nesta posição da sequencia
# abordagem não muito eficiente, pois o algoritmo tem o tempo de O(φ^n)


def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))

#############################################################################

# nesta situação, é apresentada a sequencia até o n(ésimo) número
# abordagem mais eficiente, pois o algoritmo tem o tempo de O(n)

num = 0
num_a = 1
num_b = 0
i = 0
n = 11

while i < n:
    if i == n-1:
        print(num_a)
    num = num_a + num_b
    num_b = num_a
    num_a = num
    i += 1

###########################################################################

# O algoritmo abaixo é bem mais eficiente e baseia-se na representação
# matricial da sequência de Fibonacci.
# Sua complexidade computacional é O(log n)


def fibonacci2(n):
    a = 1
    q = 1
    b = 0
    p = 0
    while n > 0:
        if (n % 2 == 0):
            qq = q*q
            q = 2*p*q + qq
            p = p*p + qq
            n /= 2
        else:
            aq = a*q
            a = b*q + aq + a*p
            b = b*p + aq
            n -= 1
    return b


print(fibonacci2(11))
