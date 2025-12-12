import math

n = int(input("Enter a number: "))
if (n % 10 == 0):
  print(n)
else:
  print(math.floor(n / 10) * 10)
