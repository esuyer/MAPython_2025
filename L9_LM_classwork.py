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
count = 0
def mult_7(A, B):
  global count
  for num in range(A, B + 1):
    if num % 7 == 0: 
      print(num)
      count += 1
mult_7(A, B)
print("There are", count, "numbers divisible by 7")