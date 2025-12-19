print("Question 1")
print("")
x=int(input("Enter a number: "))
y=int(input("Enter another number: "))
z=int(input("Enter another number: "))
odd_count = 0
if x % 2 != 0:
    odd_count += 1
if y % 2 != 0:
    odd_count += 1
if z % 2 != 0:
    odd_count += 1
print("Number of odd numbers is:", odd_count)
odd_sum=0
if x % 2 != 0:
  odd_sum += x
if y % 2 != 0:
  odd_sum += y
if z % 2 != 0:
  odd_sum += z
print("Sum of the odd numbers is:", odd_sum)
print("")
print("Question 2")
print("")
A=int(input("Give me a positive interger: "))
B=int(input("Give me a bigger interger: "))
def mult_7(A, B):
  count = 0
  for num in range(A, B + 1):
    if num % 7 == 0: 
      print(num)
      count += 1
  print("There are", count, "numbers divisible by 7")
mult_7(A, B)
print("")
print("Question 3")
print("")
Num1=int(input("Give me a positive number: "))
Num2=int(input("Give me a bigger number: "))
first_even = Num1 if Num1 % 2 == 0 else Num1 + 1
last_even = Num2 if Num2 % 2 == 0 else Num2 - 1
if first_even > last_even:
    total_sum = 0
else:
  count = (last_even - first_even) // 2 + 1
  total_sum = (count * (first_even + last_even)) // 2
print("Sum of even numbers between", Num1, "and", Num2, "is:", total_sum)