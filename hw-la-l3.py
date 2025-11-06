import random
import time
import terminal
# print("NOTE: im gonna change my typng style for a bit")
time.sleep(3)
terminal.clear()
print("Problem 1 - Random Numbers")
print("="*50)
print("")
print("I will print 2 random numbers and print their sum and difference")
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
time.sleep(1)
print("your numbers are", num1, "and", num2)
time.sleep(1)
print("and their sum is", num1 + num2, "and their difference is", num1 - num2)
time.sleep(3)
terminal.clear()
print("Problem 2 - =P")
print("="*50)
print("")
p = input("how many =P's do u want: ")
for i in range(int(p)):
  if random.randint(1,100) == 67:
    print("=D number", i + 1)
  else:
    print("=P number", i + 1)
time.sleep(3)
terminal.clear()
print("Problem 3 - DiceRoller.com")
print("="*50)
print("")
while True:
  dx = input("welcome to DiceRoller.com! type d# (# is amount of sides) to roll a dice, or type dexit to exit DiceRoller.com (not that you would want to...)! d")
  if dx == "exit":
    break
  else:
    times = input("how many times do you want to roll the d" + dx + "? ")
    for i in range(5):
      time.sleep(0.1)
      terminal.clear()
      print("◇")
      time.sleep(0.1)
      terminal.clear()
      print("□")
    for i in range(int(times)):
      print("You have rolled a", random.randint(1, int(dx)))
    time.sleep(5)
    terminal.clear()
terminal.clear()
print("Problem 3 - DiceRoller.com")
print("="*50)
print("")
