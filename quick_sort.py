"""
Quick Sort utiliza a técnica dividir para conquistar*
    -> técnica recursiva muito utilizada para resolução de problemas.
É muito mais rápido que o algoritmo de ordenação por seleção.

alguns arrays nem precisam ser ordenados, como por ex:
    array[] ou array[1]

então:
    def ordena(array):
        if array < 2:
            return array

se o array tem 2 elementos:
    def ordena(array):
        return array[0] if array[0] > array[1] else array[1]

se o elemento tem 3+ elementos podemos particionar o array escolhendo um pivô
como por ex o array[0], assim existirá um subarray[maiores] e o
subarray[menores] que poderão ser diminuídos até chegar ao caso base,
comparando apenas 2 elementos.
"""
lista = [2, 4, 1, 5, 7]


def quicksort(lista):
    if len(lista) < 2:
        return lista  # lista com 0 ou 1 elemento já estão ordenados, caso base
    else:
        pivo = lista[0]  # caso recursivo
        # list comprehencion e map
        menores = [i for i in lista[1:] if i <= pivo]
        maiores = [i for i in lista[1:] if i > pivo]

        return quicksort(menores) + [pivo] + quicksort(maiores)


print(quicksort(lista))

"""
Mas observe que se a lista já estiver ordenada, usando pivo[0] teremos o tempo
de execução tão lento quano uma pesquisa simples (pior cenário) O(n), então
pegar o pivo aleatorio na lista tem um desempenho melhor na maioria dos casos.
O(n * log n)
"""
