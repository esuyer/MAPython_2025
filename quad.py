import math
import random
import sys
import terminal
import time
print("ax²+bx+c=0")
a = float(input("a = "))
terminal.clear()
print(f"({a})x²+bx+c=0")
b = float(input("b = "))
terminal.clear()
print(f"({a})x²+({b})x+c=0")
c = float(input("c = "))
terminal.clear()
print(f"({a})x²+({b})x+({c})=0")
sure = input("is this the correct equasion (y or n): ")
terminal.clear()
if sure == "n":
  sys.exit("restart then")
speed = float(input("input the speed (1 = normal, 0 = instant)"))
terminal.clear()
print("solving for discriminant... (1/4)")
D = b ** 2
time.sleep(speed * random.randint(1,2)/(2))
terminal.clear()
print("solving for discriminant... (2/4)")
D1 = 4 * a
time.sleep(speed * random.randint(1,2)/2)
terminal.clear()
print("solving for discriminant... (3/4)")
D1 = D1 * c
time.sleep(speed * random.randint(1,2)/2)
terminal.clear()
print("solving for discriminant... (4/4)")
D = D - D1
time.sleep(speed * random.randint(1,2)/2)
terminal.clear()
print("checking for real roots... (1/1)")
time.sleep(speed * random.randint(3,5)/2)
if D < 0:
  print(f"({a})x²+({b})x+({c})=0 has no real roots")
  sys.exit("no real roots")
terminal.clear()
print("solving for positive root... (1/3)")
x1 = math.sqrt(D)
time.sleep(speed * random.randint(1,2)/2)
terminal.clear()
print("solving for positive root... (2/3)")
x1 = -b + x1
time.sleep(speed * random.randint(1,2)/2)
terminal.clear()
print("solving for positive root... (3/3)")
x1 = x1 / (2 * a)
time.sleep(speed * random.randint(3,5)/2)
terminal.clear()
print("solving for negative root... (1/3)")
x2 = math.sqrt(D)
time.sleep(speed * random.randint(1,2)/2)
terminal.clear()
print("solving for negative root... (2/3)")
x2 = -b - x2
time.sleep(speed * random.randint(1,2)/2)
terminal.clear()
print("solving for negative root... (3/3)")
x2 = x2 / (2 * a)
time.sleep(speed * random.randint(5,6)/2)
terminal.clear()
if x1 == x2:
  print(f"the roots of ({a})x²+({b})x+({c})=0 are identical, being {x1}")
else:
  print(f"the roots of ({a})x²+({b})x+({c})=0 are {x1} and {x2}")
