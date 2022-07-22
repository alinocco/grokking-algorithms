from random import randrange


def sum(array):
    sum = 0

    for e in array:
        sum += e

    return sum


def recursive_sum(array):
    if array == []:
        return 0

    return array[0] + recursive_sum(array[1:])


array = [randrange(4) for i in range(10)]

print(array)
print(sum(array))
print(recursive_sum(array))
