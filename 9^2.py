import random
num = 1
print("Problem 1\n")
v = input("Tell me a colour: ")
w = input("Tell me a colour: ")
x = input("Tell me a colour: ")
y = input("Tell me a colour: ")
z = input("Tell me a colour: ")
colour=[v, w, x, y, z]
print(colour[0], colour[4])
if "magenta" or "Magenta" in colour:
    print("Magenta is in the list")
else:
     print("Magenta is not in the list")
for i in range(len(colour)):
     print(num, colour[i])
     num = num +1
print("\nProblem 2\n")
random_list = []
for i in range(11):
 random_list.append(random.randint(-10, 10))
 print(num, random_list)
print(num, random_list)
print("\nProblem 3\n")
num1 = int(input("Give me a number: "))
python = []
for i in range(num1):
 python.append("python")
print(python)
print("\nProblem 4\n")
a = input("Give me an animal: ")
b = input("Give me an animal: ")
c = input("Give me an animal: ")
d = input("Give me an animal: ")
animal = [a, b, c, d]
print(animal)
animal[2] = "dog"
print(animal)
for i in range(len(animal)):
     animal[i] = "dog"
print(animal)
print("\nProblem 5\n")
num2 = int(input("Give me a number: "))
num3 = int(input("Give me a number: "))
num4 = int(input("Give me a number: "))
num5 = int(input("Give me a number: "))
num6 = int(input("Give me a number: "))
number = [num2, num3, num4, num5, num6]
for i in range(len(number)):
     if number[i] > 10:
         print(number[i])
print("\nProblem 6\n")
pet_animal = input("Give me a pet animal: ")
pet_animal1 = input("Give me a pet animal: ")
pet_animal2 = input("Give me a pet animal: ")
pet_animal3 = input("Give me a pet animal: ")
pet_name = input("Give me a pet name: ")
pet_name1 = input("Give me a pet name: ")
pet_name2 = input("Give me a pet name: ")
pet_name3 = input("Give me a pet name: ")
pet_animal =  [pet_animal, pet_animal1, pet_animal2, pet_animal3]
pet_name = [pet_name, pet_name1, pet_name2, pet_name3]
for i in range(len(pet_animal)):
 print(pet_name[i] + " the " + pet_animal[i])
print("\nProblem 7\n")
e = int(input("Give me any positive number: "))
list = []
for i in  range(e+1):
    list.append(i)
print(list)
print("\nProblem 8\n")
