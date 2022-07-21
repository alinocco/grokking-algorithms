# 2. Selection Sort
from random import randrange


def find_max(array, iterations):
    if array == []:
        return None

    max = array[0]
    max_index = 0

    for index, value in enumerate(array):
        iterations += 1

        if value > max:
            max = value
            max_index = index

    return max, max_index, iterations


def selection_sort(array):
    new_array = []

    iterations = 0

    for index in range(len(array)):
        iterations += 1

        max, max_index, iterations = find_max(array, iterations)
        new_array.append(array.pop(max_index))

    return new_array, iterations


array = [randrange(100000) for i in range(10)]
print(array)

print(selection_sort(array))
