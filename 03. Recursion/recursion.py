def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n-1)


while True:
    n = int(input())

    print(factorial(n))
