print("Question 1")
print("")
start=0
end=int(input("Give me a number"))
for num in range(start, end + 1):
  if num % 2 != 0:
   print(num)
print("---------")
for num in range(start, end + 1):
  if num % 2 != 0:
   print(num**2)
print("")
print("Question 2")
print("")
num1=int(input("Give me a number"))
print(num1,"till you get scared")
for num in range(num1, 0, -1):
  print(num)
if num == 1:
    print("BOO!")
  
print("")
print("Question 3")
print("")