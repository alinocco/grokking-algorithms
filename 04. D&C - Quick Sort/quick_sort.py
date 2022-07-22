from random import randrange


def quick_sort(array, pivot=0):
    # Base case
    if len(array) < 2:
        return array

    # Recursion case
    pivot = array[0]

    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)


array = [randrange(10000) for i in range(10)]
print(array)
print(quick_sort(array, randrange(len(array))))
