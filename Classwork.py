'''
print("Problem 1\n")
names = []
name = input("Enter multiple names separated by spaces: ")
names = name.split()
if names[1] == "Bob":
  print("Bob is the second name")
else:
  print("Bob is not the second name")
'''
'''
print("\nProblem 2\n")
numbers = input("Enter a list of numbers separated by commas: ")
numbers = numbers.split(",")
print(int(numbers[0]) + int(numbers[-1]))
'''
'''
print("\nProblem 3\n")
text = input("Enter a list of strings separated by commas: ")
def process_string(text):
  words = text.split(',')
  print(len(words), "words")
  for word in words:
      print(word)
process_string(text)
'''
'''
print("\nProblem 4\n")
More = input("Enter a list of numbers separated by commas: ")
Smore = More.split(",")
for i in range(len(Smore)):
  x = int(Smore[i])
  if x < 10:
    print(Smore[i])
'''
'''
print("\nProblem 5\n")
x = input("Enter 3 numbers: ")
def first(x):
  y = x.split(" ")
  print(y)
  if int(y[0]) + int(y[1]) == int(y[-1]):
    print("True")
  else:
    print("False")
first(x)
'''
'''
print("\nProblem 6\n")
evenmore = input("Enter a list of numbers: ")
evenmore = evenmore.split(" ")
evenmores = 0
for i in range(len(evenmore)):
  evenmores = evenmores + int(evenmore[i])
print(evenmores)
'''
'''
print("\nProblem 7\n")
expression = input("Enter a operation followed by two numbers: ")
def compute(expression):
  parts = expression.split(' ')
  symbol = parts[0]
  num1 = int(parts[1])
  num2 = int(parts[2])

  if symbol == '+':
      return num1 + num2
  else:
      return num1 - num2
print(compute(expression))
'''
print("\nProblem 8\n")
text = input("Give me several words separated by spaces: ")
words = text.split(' ')
for word in words:
    if len(word) > 0:
        if word[0].lower() == word[-1].lower():
            print(word)

