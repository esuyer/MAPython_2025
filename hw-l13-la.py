import random
import time
import terminal
print("im gonna give you a list of random numbers:")
time.sleep(1)
rands = []
for i in range(5):
  rands.append(random.randint(1,10))
print(rands)
time.sleep(1)
print(f"the first and last numbers added together (aka {rands[0]}, and {rands[-1]})")
print("heres them on each row:")
time.sleep(0.5)
for i in rands:
  print(i)
  time.sleep(0.1)
time.sleep(1)
for i in rands:
  if i % 2 == 0:
    rands.remove(i)
print("and heres only the odd ones:")
time.sleep(0.5)
for i in rands:
  print(i)
  time.sleep(0.2)
time.sleep(1)

print("\nnext\n")

time.sleep(1)
print("wait...")
time.sleep(1)
print("you're organizing a party! who are you inviting?")
time.sleep(1)
invited = []
for i in range(int(input("but first, how many people are you inviting? "))):
  invited.append(input("who are you inviting? "))
time.sleep(1)
print("wait, i can do this, right?")
time.sleep(1.5)
print(f"who are you inviting? {terminal.machine.name}")
invited.append(terminal.machine.name)
time.sleep(1)
print(f"so you are inviting these people: {invited}?")
time.sleep(1)
print("ok!")
time.sleep(1)

print("\nnext\n")

time.sleep(1)
num = int(input("how many pulses do you want"))
count = 0
pulses = []
for i in range(num):
  count += 1
  pulses.append("+" * count)
print("here ya go \n", pulses)
