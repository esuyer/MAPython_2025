def multiply_by_1000(N):
    result = 0
    for _ in range(1000):
        result += N
    print("1000 ×", N, "=", result)

def power_of_five(N):
    result = 1
    for _ in range(N):
        result *= 5
    print("5 ^", N, "=", result)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(n, "factorial =", result)

def sum_fractions(N):
    total = 0
    for i in range(1, N + 1):
        total += 1 / i
    print("Sum of fractions up to", N, "=", total)

def sum_neighbors(N):
    total = 0
    for i in range(1, N):
        total += i * (i + 1)
    print("Sum of neighbors up to", N, "=", total)

N1 = int(input("Enter a positive number: "))
multiply_by_1000(N1)

N2 = int(input("Enter a non-negative integer: "))
power_of_five(N2)

N3 = int(input("Enter a non-negative number: "))
factorial(N3)

N4 = int(input("Enter a positive number: "))
sum_fractions(N4)

N5 = int(input("Enter a positive number: "))
sum_neighbors(N5)
