from random import randrange


def length(array):
    length = 0

    for e in array:
        length += 1

    return length


def recursive_length(array):
    if array == []:
        return 0

    return 1 + recursive_length(array[1:])


array = [randrange(4) for i in range(10)]

print(array)
print(length(array))
print(recursive_length(array))
