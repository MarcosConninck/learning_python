# Por Marcos Conninck, estudo do livro: "Entendendo Algoritmos:
# Um Guia Ilustrado Para Programadores e Outros Curiosos
# Algoritmo de pesquisa binária
###################################################################
"""
This algorithm is a fastest way to find a number in a orderd list. O(log n)
Better than check all numbers in the list, O(n)
"""

list = list(range(0, 1001))
number_to_be_found = int(
    input('Input one number between 0 - 1000 to be found: '))


def binary_search(list, item: int):
    attempt = 0
    low = 0
    high = len(list) - 1

    while low <= high:
        # middle element
        middle = (low + high) // 2
        attempt = attempt + 1
        print(f'trying = {middle}, attempt = {attempt}')
        trying = list[middle]
        if trying == item:
            # found
            print(f'number found... "{middle}" in {attempt} attempts')
            return middle
        if trying > item:
            high = middle - 1
            # Higher-than-expected
        else:
            low = middle + 1
            # Lower-than-expected
    print("Number isn't in the range")
    return None
    # number doesn't exist


binary_search(list, number_to_be_found)
