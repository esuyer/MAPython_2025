print("Question 1")
print("")
n1=int(input("Give me a number"))
n2=int(input("Give me another number"))
print(n1,n2)
if n1 >=1 and n2 >=1:
  print("both numbers are posiive")
else:
  print("I wanted both to be positive")
print("")
print("Question 2")
print("")
num1=int(input("Give me a number"))
num2=int(input("Give me another number"))
print(num1,num2)
if num1 >=1 or num2 >=1:
  print("at least one of the numbers is positive")
else:
  print("I wanted at least one to be positive")
print("")
print("Question 3")
print("")
LuckNum=int(input("Give me a number"))
if LuckNum == 7 or LuckNum == 77:
  print("lucky number")
else:
  print("regular number")
print("")
print("Question 4")
print("")
Num3=int(input("Give me a 3 digit number"))
if Num3 >=100 and Num3 <1000:
  print("Thanks")
else:
  print("That is not what I wanted")
print("")
print("Question 5")
print("")
Num4=int(input("Give me a number"))
Num5=int(input("Give me another number"))
if (Num4 >0) ^ (Num5 >0):
  print("exactly one of the number is positive")
else:
  print("I wanted exactly one of the numbers to be positive")