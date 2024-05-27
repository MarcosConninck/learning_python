from functools import reduce
from typing import Any
"""
Mais 10 algoritmos.

    Árvore binária

Nós à esquerda têm valores menores, nós da direita possuem valores maiores.
A pesquisa se inicia pelo nó raiz, e toma o caminho a esquerda ou a direita
comparando com o valor que esta sendo buscado (similar a pesquisa binária)
É mais rápida para inserções e remoções que um array, em média

          array      arvore binária de busca
busca    O(log n)    O(log n)
inserção O(n)        O(log n)
remoção  O(n)        O(log n)

Entretanto também têm algumas desvantagens, não é possivel autilizar acesso
aleatório, como por exemplo "selecione o quinto elemento da arvore".
O tempo de execução é fortemente dependente da arvore estar balanceada.

São geralmente utlizadas para armazenar dados em BD.
Mais temas relacionados a arvore binária de busca:
-> árvores B
-> árvores rubro-negras (red-black tree)
-> heaps
-> árvores splay (espalhadas)
"""
###############################################################################

#    Índices invertidos

tabela_hash: Any = {}
a = set(["oi", "lá"])
b = set(["oi", "adit"])
c = set(["oi", "lá", "vamos", "nós"])
tabela_hash["oi"] = a, b
tabela_hash["lá"] = a, c
tabela_hash["adit"] = b
tabela_hash["vamos"] = c
tabela_hash["nós"] = c
print(tabela_hash)

# um usuário buscando a palavra "oi" receberá de resposta as páginas A e B
# Esta estrutura de dados é muito util, já que uma hash mapeia palavras para
# lugares onde elas aparece. Esta estrutura é chamado de índice invertido.

###############################################################################
"""
    A Transformada de Fourier

É um dos raros algoritmos que conseguem ser brilhantes, elegantes e ter
milhares de forma de utilização.
Dado uma vitamina, por exemplo, este algoritmo informa os ingredientes desta
vitamina.
Dado uma música, este algoritmo separa as frequencias individuais.

Este é o modo de funcionamento do mp3, JPG, prever terremotos e analisar DNA.
"""

###############################################################################
"""
    Algoritmos Paralelos

Antigamente não tinhamos processadores com tantos núcleos, mas agora para que
o algoritmo se torne mais rápido, é necessario fazer com que ele seja executado
paralelamente, em todos os núcleos de uma só vez.

-> gerenciamento de paralelismo:
    Imagine ordenar um array de 1000 itens, fornecer 500 arrays cada um dos
    núcleos e depois ordena-los.
-> balanceamento de carga:
    Suponha 10 tarefas que devam ser executadas, então cada núcleo recebe 5.
    Mas o núcleo A recebeu tarefas simples e terminou em segundos, enquanto o
    nucleo B recebeu tarefas complexas e demorou minutos.

###############################################################################

    Map Reduce

O algorimo distribuido -> apache Hadoop
Algoritmo para executar em diversas máquinas, utilizando vários núcleos

###############################################################################

    Porque algoritmos distribuidos são uteis:
    -> Uma tabela hash com bilhoes de linhas, para fazer uma consulta SQL
    complexa na tabela, mas existem problemas quando se consulta milhoes de
    linhas, sendo assim é conveniente utilizar Map Reduce por itermédio do
    Hadoop.

    -> Imagine processar uma longa lista de tarefas, em uma máquina poderia
    levar meses, mas em várias maquinas poderia levar apenas dias.
"""

###############################################################################

#   Função Map

# A função map é muito simples, ela pega um array e aplica a mesma função para
# cada item no array, como por exemplo:

arr1 = [1, 2, 3, 4, 5]
arr2 = map(lambda x: 2 * x, arr1)
new_arr2 = []
for i in arr2:
    new_arr2.append(i)
print(f'map: {new_arr2}')

###############################################################################

#   Função Reduce

# função map vai de um arr para outro
# funçaõ reduce é reduzir uma lista inteira para apenas um item

arr3 = reduce(lambda x, y: x+y, arr1)
print(f'reduce: {arr3}')

# MapReduce usa dois conceitos simples para executar consulta de dados em
# diversas máquinas. Pode fornecer uma resposta rápida, quando tratando de
# bilhoes de linhas. Enquanto o BD pode demorar muito.

###############################################################################

"""
    Filtro de Bloom e HyperLogLog

Imagine que estamos administrando o Reddit:
-> verificar se já não foi postado antes.
Rastrear página no google:
-> verificar se já não foi rastreada antes.

ou seja,

um conjunto muito grande para pesquisar, para apenas encontrar um item

    Filtros de Bloom

São uma estrutura de dados probabilística que fornece resposta que pode estar
errada, mas provavelmente estará correta.
Em vez de utilizar uma hash, é possivel perguntar a um filtro bloom se uma URL
já foi rastreada antes.
Hash daria a resposta exata, mas ocupa muito espaço.

Falsos positivos são possiveis
Falsos negativos não são possiveis

Muito leve e util quando não é necessário uma resposta exata, como visitando
um URL duvidoso: "este site pode ser malicioso"

    HiperLogLog

No mesmo estilo dos filtros de bloom.
O HiperLogLog aproxima o numero de elementos unicos em um conjunto. Assim como
o filtro de bloom, ele não fornecerá uma resposta exata, mas se aproximará
muito, usando apenas uma fração da memoria.
Como por exemplo uma pesquisa que nunca foi feita no google.

###############################################################################

    Algoritmos SHA

    Comparando Arquivos:

Secure Hash Algorithm
Dada uma str, o SHA retorna uma hash para esta string.
"ola" => 2fc24bd...
O SHA é uma função hash. Ele gera um hash, que é apenas uma string curta, ela
gera uma string diferente para cada string de entrada.
A função hash faz a ligação entre string e indice de arrays
O SHA faz a ligação entre string e string.

Muito úteis para verificar se dois arquivos são iguais, especialmente quando
são arquivos grandes.

    Verificando Senhas:

Util para comparar strings sem revelar a string original
pois cada string tem um valor hash SHA, então a senha do email não fica
armazenada de forma literal no BD do site, mas apenas o valor hash SHA e não
é possivel descobrir a string original a partir da hash.
Na verdade são uma família de algoritmos -> SHA-0, SHA-1, SHA-2, SHA-3

    Hash sensitivo local (Simhash):

Ele é localmente insensitivo.
mão -> dc6573
mãe -> e329ad -> totalmente diferente
Isto é bom para não comparar hashes para verificar se a senha está perto de ser
quebrada.

Porém às vezes você quer comparar hash entre si, para detectar pequenas
mudanças nas strings e verificar o quanto são semelhantes.

Detectar duplicatas
Verificar se um aluno copiou um trabalho da internet
Um site poderia filtrar uploads de livros que tenham direitos autorais,
utilizando simhash

    Troca de chaves de Diffie-Hellman:

Criptografia de mensagens
Chave publica - chave privada
Sucessor -> RSA

    Programação Linear:

A programação linear é usada para maximizar algo em relação a um limite
por exemplo:
camiseta - 1m tecido - 5 botoes - 2$ lucro
bolsas   - 2m tecido - 2 botoes - 3$ lucro
Quantas camisetas e bolsas fabricar para maximizar o lucro?
limite é a quantidade de material disponível.

Algoritmos de grafos podem ser feitos por meio de programação linear.
É um framework mais geral, grafos são apenas um subconjunto.

Utiliza o algoritmo Simplex:
O algoritmo Simplex é um procedimento iterativo para resolver problemas de pl
em um número finito de etapas. Consiste em: i) Conhecer uma solução básica
viável inicial; ii) Testar se a solução é ótima; iii) Melhorar a solução
a partir de um conjunto de regras e repetir o processo até que uma solução
ótima seja obtida.
"""
