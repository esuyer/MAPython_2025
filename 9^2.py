a = int(input("Give me a number: "))
b = int(input("Give me a number: "))
c = int(input("Give me a number: "))
print(a, b, c)
odd_count = 0
odd_sum = 0
for x in [a, b, c]:
    if x % 2 != 0:
        odd_count += 1
        odd_sum += x
print("There are", odd_count, "odd numbers")
print("Their sum is", odd_sum)
A = int(input("Give me a positive integer: "))
B = int(input("Give me a bigger integer: "))
count = 0
for i in range(A, B + 1):
    if i % 7 == 0:
        print(i)
        count += 1
print("There are", count, "numbers divisible by 7")
A = int(input("Give me a positive integer: "))
B = int(input("Give me a bigger integer: "))
total = 0
for i in range(A, B + 1):
    if i % 2 == 0:
        total += i
print("The sum of even numbers from", A, "to", B, "is", total)
def sum_squares(N):
    total = 0
    for i in range(1, N + 1):
        total += i * i
    print(total)
sum_squares(5)
sum_squares(10)
A = int(input("Give me a positive 2-digit number: "))
B = int(input("Give me a bigger positive 2-digit number: "))
count = 0
for i in range(A, B + 1):
    first_digit = i // 10
    last_digit = i % 10

    if first_digit + last_digit > 10:
        print(i)
        count += 1
print("Got", count, "numbers")
N = int(input("Give me a positive integer: "))
def sum_first_n_odds(N):
    total = 0
    odd = 1
    for _ in range(N):
        total += odd
        odd += 2
    print(total)
sum_first_n_odds(N)
sum_first_n_odds(N+6)
