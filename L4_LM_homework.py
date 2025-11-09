import random

print("Question 1")
print("")
Num1=(int(input("Give me a number")))
Num2=(int(input("Give me another number")))
if  Num1>Num2:
    print(Num2)
if  Num2>Num1:
    print(Num1)
print("Question 2")
print("")
Age= int(input("How old are you?"))
if Age>=16:
    print("The price of the ticket is $8")
elif Age<=15 and Age>2:
    print("The price of the ticket is $5")
if Age<=2:
    print("The price of the ticket is $0")
print("Question 3")
print("We rolled a six sidded dice")
roll = random.randint  (1,6)
if  roll > 3:
    print("You are doing homework!")
else:
  print("You are having lunch!")
  x = int(input("Enter a number:"))
  if x % 2 == 0:
    print("You are having cake!")
  else:
    print("You are having spinache!")
print("Question 4")
print("")
Num4=(int(input("Give me a number")))
if Num4 % 10 == 0:
    print("The number is ends with 0")
else:
    print("The number does not end with 0")
print("Question 5")
print("")
c=int(input("Enter another number: "))
a=c
b=int(input("Enter a number: "))
print(a,b)
print("Swapped:")
a=b
b=c
print(a,b)
print("Question 6")
print("")
candy=int(input("How many candies do you have?"))
kids=int(input("How many kids are there?"))
answer=kids%candy
print("each kid will have",answer,"candies")