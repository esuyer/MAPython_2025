print("Question 1")
print("")
print("a)")
num1=int(input("Give me a number between 10 and 20,"))
if num1 >=10 and num1 <=20:
  print("Thank you")
else:
  print("That is not what I wanted")
print("b)")
num2=int(input("Give me another number between 10 and 20,"))
if num2==10 or num2<=20:
  print("Thank you")
else:
  print("That is not what I wanted")
print("")
print("Question 2")
print("")
A=int(input("Give me a number"))
B=int(input("Give me another number"))
if A+B==50 or A*B==100:
  print(A,B, "are a good pair")
else:
  print(A,B, "are not a good pair")
print("")
print("Question 3")
print("")
month=str(input("Give me a month"))
day=int(input("Give me a day"))
if month=="October" and day==31:
   print("BOO!")
elif month=="November" and day==26:
   print("Gobble, gobble!")
else:
   print("A nice day")
print("")
print("Question 4")
print("")
Num4=int(input("Give me a non-zero number"))
Num5=int(input("Give me another non-zero number"))
if Num4>0 and Num5>0:
   print("same sign")
elif Num4<0 and Num5<0:
   print("same sign")
else:
   print("NOT the same sign")
print("")
print("Question 5")
print("")
N= int(input("Give me a non-negative interger"))
if N<=2 or N>=8:
   print("Close")
else:
   print("Far")
print("")
print("Question 6")
print("")
num6=int(input("Give me a number from 1 to 8"))
num7=int(input("Give me another number from 1 to 8"))
if num6==num7 or num6+num7==9:
   print(num6,num7,"are on the big diagonal")
else:
   print(num6,num7,"are NOT on the big diagonal")