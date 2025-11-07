import random
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
if num1 > num2:
  print(num2)
elif num2 == num1:
  print(num1)
else:
 print(num1)
num3 = int(input("Enter a number: "))
num4 = int(input("Enter another number: "))
if num3 > num4:
   print(num4)
elif num4 == num3:
   print(num3)
else:
   print(num3)
age = int(input("How old are you? "))
if age < 2:
      print("The cost of the ticket is 0")
else:
 if age <= 15:
          print("The cost of the ticket is 5")
 else:
          print("The cost of the ticket is 8")

print("We roll a 6 sided die")
roll = random.randint(1, 6)
if roll == 3:
   print("You need to do homework!")
else:
   print("You are having lunch!")
food = int(input("Enter a number:"))
if food % 2 == 0:
   print("You are having cake!")
else:
   print("You are having spinach!")

num5 = int(input("Enter a number: "))
if num5 % 10 == 0:
   print("This number ends in 0!")
else:
   print("This number does not end in 0!")

c = int(input("Enter a number: "))
a = c
b = int(input("Enter another number: "))
print(a,b)
a = b
b = c
print("Swapped:")
print(a,b)

c = int(input("candies: "))
k = int(input("kids: "))
print(0 if c % k == 0 else k - c % k)