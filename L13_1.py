import random

print ("Problem 1")
colors = ['green', 'blue', 'red', 'orange']
print("The first color is ", colors[0])
print("The last color is ", colors[len(colors)-1])

if "magenta" in colors: 
   print("Found magenta")
else:
   print("Did not find magenta")

for i in range(len(colors)):
   print(i+1, colors[i])

"""
Problem 2. 5 random numbers
Create an empty list and add 5 random integers between -10 and 10 to it (use function append). Print
the list.
"""
print ("Problem 2")
numbers = []
for i in range(5):
   numbers.append(random.randint(-10, 10))

print(numbers)

"""
Problem 3. More Python
Ask the user for an integer N. Create an empty list and add N words “Python” to it. Print the list.
Example:
Give me an integer: 5
[&#39;Python&#39;, &#39;Python&#39;, &#39;Python&#39;, &#39;Python&#39;, &#39;Python&#39;
"""
print ("Problem 3")
n = int(input("Give me an integer: "))
words = []
for i in range(n):
   words.append("Python")

print(words)

"""
Problem 4. Animals
Create a list of animals that has at least 4 animals in it. Print it.
Example:
[&#39;owl&#39;, &#39;horse&#39;, &#39;pig&#39;, &#39;donkey&#39;]
a) Change the 3rd animal to “cat” (use [] notation). Print the list.
b) Now, change all elements in the list to “dog”. Print the list.
Example:
[&#39;owl&#39;, &#39;horse&#39;, &#39;cat&#39;, &#39;donkey&#39;]
[&#39;dog&#39;, &#39;dog&#39;, &#39;dog&#39;, &#39;dog&#39;]
Tip: in 4b we need to do the same action (changing the value to “dog”) for all the elements of a
list, so we need to loop through the list and change each element.
"""

print ("Problem 4")
animals = ['owl', 'horse', 'pig', 'donkey']
print(animals)
animals[2] = "cat"
print(animals)
for i in range(len(animals)):
   animals[i] = "dog"

print(animals)

"""
Problem 5. Greater than 10
Create a list of numbers. Print it.
Print only numbers that are greater than 10.
Example:
[-4, 1000, 3.5, 10, 11.8]
1000
11.8
Tip: if stuck, start with printing all numbers, one per line. Then, add a condition to printing.
"""
print ("Problem 5")
numbers = [-4, 1000, 3.5, 10, 11.8]
print(numbers)
for i in range(len(numbers)):
   if numbers[i] > 10:
      print(numbers[i])

"""
Problem 6. Pets
Create 2 lists of the same length: pet types (cats, dogs etc.) and their names. The 1 st name belongs to
the 1 st pet, the 2 nd name belongs to the 2 nd pet, and so on.
a) Print the lists
For each pet print the information about it in format “______ the ________”
(pet name) (pet type)
Example:
[&#39;cat&#39;, &#39;dog&#39;, &#39;alligator&#39;, &#39;fly&#39;]
[&#39;Fluffs&#39;, &#39;Fido&#39;, &#39;Annie&#39;, &#39;Fanny&#39;]
Fluffs the cat
Fido the dog
Annie the alligator
Fanny the fly
b) Modify the code from 6a so it adds pet information to a new list and prints this list.
Example:
[&#39;Fluffs the cat&#39;, &#39;Fido the dog&#39;, &#39;Annie the alligator&#39;, &#39;Fanny the fly&#39;]
"""
print( "Problem 6")
pet_types = ['cat', 'dog', 'alligator', 'fly']
pet_names = ['Fluffs', 'Fido', 'Annie', 'Fanny']
print(pet_types)
print(pet_names)
for i in range(len(pet_types)):
   print(pet_names[i], "the", pet_types[i])

pet_info = []
for i in range(len(pet_types)):
   pet_info.append(pet_names[i] + " the " + pet_types[i])
   print(pet_info[i])
  
print(pet_info)
  
  



  
