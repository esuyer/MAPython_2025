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
  
"""
Problem 7. 0 to N
Ask the user for a positive integer N. Create a list that contains all integers from 0 to N (inclusive).
Print the list.
Example:
Give me an integer: 10
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Tip: start with an empty list.
"""  
print  ("Problem 7")
n = int(input("Give me an integer: "))
numbers = []
for i in range(n+1):
   numbers.append(i)

print(numbers)

"""
Problem 8. Trip planner
Create a list of 5 city names of your choice for the user to visit. Print the list.
Ask the user if they want to make any changes.
If the user’s answer is “yes”, your program should do the following:
 Ask the user for an integer number between 0 and 4 (inclusive), N.
 Ask the user for a new destination.
 Change the city in the list that stands at position N to the destination that the user entered.
 Print the changed list.
Examples:
[&#39;New York&#39;, &#39;Paris&#39;, &#39;Seattle&#39;, &#39;Tokyo&#39;, &#39;Moscow&#39;]
Do you want to make any changes to your trip? yes
Give me an integer between 0 and 4: 2
Give me a new destination: London
[&#39;New York&#39;, &#39;Paris&#39;, &#39;London&#39;, &#39;Tokyo&#39;, &#39;Moscow&#39;]
&#39;Tokyo&#39;, &#39;Moscow&#39;]
"""
print  ("Problem 8")
cities = ['New York', 'Paris', 'Seattle', 'Tokyo', 'Moscow']
print(cities)
answer = input("Do you want to make any changes to your trip? ")
if answer == "yes":
   n = int(input("Give me an integer between 0 and 4: "))
   new_destination = input("Give me a new destination: ")
   cities[n] = new_destination
   print(cities)

"""
Problem 9. Split the line
You are given a list of names – people standing in line to a ticket booth. Another
ticket booth just opened, and your job is to split the original line into two as fair as
possible – the people at even positions go to one line and the people at odd
positions go to another.
Write a function with one parameter: a list of names. This function should create and print two new
lists – names of people in two new lines. Your function should not change the original list.

Examples:
Function call Output
split_line([&#39;Joe&#39;, &#39;Ann&#39;, &#39;Bob&#39;, &#39;Kathy&#39;, &#39;Mary&#39;, &#39;Billy&#39;]) [&#39;Joe&#39;, &#39;Bob&#39;, &#39;Mary&#39;]
[&#39;Ann&#39;, &#39;Kathy&#39;, &#39;Billy&#39;]
split_line([&#39;Tony&#39;, &#39;Sam&#39;, &#39;Mike&#39;]) [&#39;Tony&#39;, &#39;Mike&#39;]

[&#39;Sam&#39;]
"""
print  ("Problem 9")
def split_line(names):
   line1 = []
   line2 = []  
   for i in range(len(names)):
      if i % 2 == 0:
         line1.append(names[i])
      else:
         line2.append(names[i])

   print(line1)
   print(line2)

split_line(['Joe', 'Ann', 'Bob', 'Kathy', 'Mary', 'Billy'])
split_line(['Tony', 'Sam', 'Mike'])

"""
Problem 10. Merge the lines (challenge)

Prime Factor Math Circle 2024-2025

© 2024 Prime Factor Math Circle. Property of Prime Factor Math Circle.
You are given two lists of names – people standing in line to two ticket booths. The second ticket
booth just closed, and your job is to merge the original lines into one as fair as possible:
 the 1 st person from the 1 st line
 the 1 st person from the 2 nd line
 the 2 nd person from the 1 st line
 the 2 nd person from the 2 nd line
 and so on.
If one line is longer that the other, the remaining people from that line should go to the end of the new
line in the same order they were in the original line.
Write a function with two parameters: two lists of names. This function should create and print a new
list – names of people in the new line. Your function should not change the original two lists.
Examples:
Function call Output
merge_lines([&#39;Ann&#39;, &#39;Andrew&#39;, &#39;Alice&#39;, &#39;Alex&#39;, &#39;Arie&#39;],
[&#39;Bob&#39;, &#39;Ben&#39;])

[&#39;Ann&#39;, &#39;Bob&#39;, &#39;Andrew&#39;, &#39;Ben&#39;,
&#39;Alice&#39;, &#39;Alex&#39;, &#39;Arie&#39;]

merge_lines([&#39;Bob&#39;, &#39;Ben&#39;],
[&#39;Ann&#39;, &#39;Andrew&#39;, &#39;Alice&#39;, &#39;Alex&#39;, &#39;Arie&#39;])

[&#39;Bob&#39;, &#39;Ann&#39;, &#39;Ben&#39;, &#39;Andrew&#39;,
&#39;Alice&#39;, &#39;Alex&#39;, &#39;Arie&#39;]

merge_lines([&#39;Bob&#39;, &#39;Ben&#39;, &#39;Bettany&#39;],
[&#39;Ann&#39;, &#39;Andrew&#39;, &#39;Alice&#39;])

[&#39;Bob&#39;, &#39;Ann&#39;, &#39;Ben&#39;, &#39;Andrew&#39;,
&#39;Bettany&#39;, &#39;Alice&#39;]
"""

print  ("Problem 10")
def merge_lines(line1, line2):
   new_line = []
   for i in range(len(line1)):
      new_line.append(line1[i])
      if i < len(line2):
         new_line.append(line2[i])

   if len(line2) > len(line1):
      for i in range(len(line1), len(line2)):
         new_line.append(line2[i])

   print(new_line)

merge_lines(['Ann', 'Andrew', 'Alice', 'Alex', 'Arie'], ['Bob', 'Ben'])
merge_lines(['Bob', 'Ben'], ['Ann', 'Andrew', 'Alice', 'Alex', 'Arie'])
merge_lines(['Bob', 'Ben', 'Bettany'], ['Ann', 'Andrew', 'Alice'])
merge_lines(['Ann', 'Andrew', 'Alice', 'Alex', 'Arie'], ['Bob', 'Ben', 'Bettany'])
merge_lines(['Bob', 'Ben', 'Bettany'], ['Ann', 'Andrew', 'Alice', 'Alex', 'Arie'])
merge_lines(['Bob', 'Ben', 'Bettany', 'Beth'], ['Ann', 'Andrew', 'Alice', 'Alex', 'Arie'])
merge_lines(['Ann', 'Andrew', 'Alice', 'Alex', 'Arie'], ['Bob', 'Ben', 'Bettany', 'Beth'])
