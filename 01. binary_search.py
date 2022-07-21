# 1. Binary Search

def binary_search(array, value):
    iterations = 0

    left = 0
    right = len(array)

    while left <= right:
        iterations += 1

        middle = (left + right) // 2
        guess = array[middle]

        if guess == value:
            return middle, iterations

        if guess > value:
            right = middle - 1
        else:
            left = middle + 1

    return None, iterations


array = [x for x in range(1, 100000, 2)]

while True:
    try:
        value = int(input("Enter the looked number: "))
        index, iterations = binary_search(array, value)

        print("Index:", '%10s' % index)
        print("Iterations:", '%10s' % iterations)
    except:
        print("Thank you for testing, waiting for you coming back!!!")
        break
