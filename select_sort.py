# This algorithm was developed to improve my coding skills.
# In this case, i will make a program to ordenate a list

# first of all, in a list, we need to find the lower element, and its index
# at second, append it to a new list
list1 = [10, 20, 9, 30]
list2 = [10, 20, 30, 9]
list3 = [9, 10, 20, 30]


def find_lower(lista):
    lower_number = lista[0]  # save the lower value
    lower_index = 0  # save the index of the lower value
    for i in range(len(lista)):
        if lista[i] < lower_number:
            lower_number = lista[i]
            lower_index = i
    return lower_index


def sort_by_selection(lista):
    new_list = []
    for i in range(len(lista)):
        lower_number = find_lower(lista)
        new_list.append(lista.pop(lower_number))
    return new_list


print(f'unordered list1: {list1}')
print(f'ordered list1 {sort_by_selection(list1)}\n')
print(f'unordered list2: {list2}')
print(f'ordered list2 {sort_by_selection(list2)}\n')
print(f'unordered list3: {list3}')
print(f'ordered list3 {sort_by_selection(list3)}')
