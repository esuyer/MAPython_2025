import time
def factorial(n):
  total = 1
  if not n == 0:
    for i in range(1,n+1):
      total = total * i
  else:
    total = 0
  return total
def sumofrac(n):
  total = 1
  for i in range(1, n+1):
    total += 1/n
  return total
n = int(input("give me a number: "))
total = 0
for i in range(0,1000):
  total += n
print(n,"x 1000 =", total)
time.sleep(1)
total = 1
n = int(input("give me another number: "))
for i in range(1, n + 1):
  total = total * 5
print("5 ^", n, "=", total)
time.sleep(1)
print("the number you chose! =", factorial(int(input("give me yet another number: "))))
time.sleep(1)
print("1 + 1/2 + 1/3 +...+ 1/the number you chose =", sumofrac(int(input("give me another number again: "))))
time.sleep(1)
n = int(input("you know the drill: "))
total = 0
for i in range(1, n+1):
  total += i * i+1
print(total)
time.sleep(2)
print("ok now on to the other stuff")
time.sleep(1)
count = 0
total = 0
n = int(input("give me 3 numbers (1/3): "))
nn = int(input("give me 3 numbers (2/3): "))
nnn = int(input("give me 3 numbers (3/3): "))
if n % 2 == 1:
  count += 1
  total += n
if nn % 2 == 1:
  count += 1
  total += nn
if nnn % 2 == 1:
  count += 1
  total += nnn
print("there are", count, "odd numbers with", total, "as their sum")
time.sleep(1)
n = int(input("now give me a word..., just kidding! give me a number: "))
print("i wasnt doen... ", "e" * 100000000000000)
