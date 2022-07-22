def tail_factorial(n, calculated=1):
    if n == 1:
        return calculated

    return tail_factorial(n - 1, n * calculated)


while True:
    n = int(input())

    print(tail_factorial(n))
