from random import randrange


def max(array):
    if len(array) == 0:
        return 0

    if len(array) == 1:
        return array[0]

    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]

    additional_max = max(array[1:])
    return array[0] if array[0] > additional_max else additional_max


array = [randrange(1000) for i in range(100)]
print(array)
print(max(array))
