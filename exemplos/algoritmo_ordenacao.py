# Visível no print o que está acontecendo com lista antiga e a nova
lista = [8, 3, 2, 5, 10, 20, 6, 2]


def encontra_menor(lista):
    menor_numero = lista[0]
    menor_indice = 0
    for i in range(len(lista)):
        if lista[i] < menor_numero:
            menor_numero = lista[i]
            menor_indice = i
    return menor_indice


def ordena_lista(lista):
    nova_lista = []
    for i in range(len(lista)):
        menor_indice = encontra_menor(lista)
        print(f'menor índice da lista antiga é: lista[{menor_indice}], '
              f'ou seja {lista[menor_indice]}')
        print(f'lista antiga: {lista}')
        nova_lista.append(lista.pop(menor_indice))
        print(f'nova lista: {nova_lista}')
        print()
    return nova_lista


print('Lista original: ', lista)
print(ordena_lista(lista))
