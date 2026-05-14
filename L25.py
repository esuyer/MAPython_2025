'''
pet_list = ['dog', 'dog', 'dog', 'cat', 'cat', 'bird' , 'bird', 'bird', 'snake', 'snake', 'snake','dog', 'dog', 'dog', 'cat', 'cat', 'bird' , 'bird', 'bird', 'snake', 'snake']

d = {}
for pet in pet_list:
  if pet in d:
    d[pet] += 1
  else:
    d[pet] = 1

print(d)
'''
'''
address = "www.wikipedia.org"
addressParts = address.split(".")
print(addressParts)
'''

'''
print("bananas".split("a"))
'''

'''
print("1<>2<>3<>4<>5".split("<>"))
'''

'''
print("2 4 70 3".split(" "))
'''

'''
parts = ["I", "love", "Python"]
sentence = " ".join(parts)
print(sentence)
'''

'''
In each problem print the list after splitting a string to make sure that the result is what you expected.
Problem 1. Names
Ask the user for a string that has several names separated by single spaces.
Split it into a list of names (split by spaces) and print the result.
Check if the second name is “Bob”. If there is no second name, print “There is no second name”.
Examples:
Give me several names separated by spaces: Joe Bob Sally
[&#39;Joe&#39;, &#39;Bob&#39;, &#39;Sam&#39;]
The second name is Bob.
Give me several names separated by spaces: Bob Sam Sally
[&#39;Bob&#39;, &#39;Sam&#39;, &#39;Joe&#39;]
The second name is not Bob.
'''
print("Problem 1")
names = input("Give me several names separated by spaces: ")
names_list = names.split(" ")
print(names_list)
if len(names_list) >= 2 and names_list[1] == "Bob":
  print("The second name is Bob.")
else:
  print("The second name is not Bob.")


'''
Problem 2. Numbers
Ask the user for a string that has several integers separated by commas.
Split it by commas and print the result.
Print the sum of the first and the last integers.
Example:
Give me a several integers separated by commas: 2,10,3,5
[&#39;2&#39;, &#39;10&#39;, &#39;3&#39;, &#39;5&#39;]
7
Tip: split(&quot;,&quot;) is useful here.
'''
print("Problem 2")
numbers = input("Give me a several integers separated by commas: ")
numbers_list = numbers.split(",")
print(numbers_list)
sum = int(numbers_list[0]) + int(numbers_list[-1])
print(sum)


'''
Problem 3. How many words?
Write a function with 1 parameter: a string of words separated by single spaces. This function should:
a) Print how many words there are in the string.
b) Print the words so that each word is on its own line.
Examples:
String Output
&#39;March April May&#39; 3 words
March
April
May
&#39;one two three four&#39; 4 words
one
two
three
four
'''
print("Problem 3")
def how_many_words(words):
  words_list = words.split(" ")
  print(len(words_list), "words")
  for word in words_list:
    print(word)

how_many_words("March April May")

how_many_words("one two three four")



'''
Problem 4. Small numbers
Ask the user for a string that has several integers separated by commas.
Print the numbers that are less than 10 (one per line)
Example:
Give me a several integers separated by commas: 2,100,33,5,10
2
5
'''
print("Problem 4")
numbers = input("Give me a several integers separated by commas: ")
numbers_list = numbers.split(",")
for number in numbers_list:
  if int(number) < 10:
    print(number)
    break



  

'''
Problem 5. Three numbers
Write a function with 1 parameter: a string that has 3 integers separated by single spaces. This
function should return True if the sum of the first two numbers is equal to the third number.
Otherwise, it should return False.
Examples:
three_nums(&#39;1 1 2&#39;)  True
three_nums(&#39;12 3 20&#39;)  False
three_nums(&#39;4 10 14&#39;)  True
three_nums(&#39;100 200 300&#39;)  True
'''
print("Problem 5")
def three_nums(numbers):
  numbers_list = numbers.split(" ")
  if int(numbers_list[0]) + int(numbers_list[1]) == int(numbers_list[2]):
    return True
  else:
    return False

print(three_nums("1 1 2"))
print(three_nums("12 3 20"))
print(three_nums("4 10 14"))
print(three_nums("100 200 300"))



'''
Problem 6. Sum of numbers
Ask the user for a string that has several integers separated by single spaces.
Compute and print the sum of the numbers.
Example:
Give me several integers separated by spaces: 2 10 3 5
20
'''
print("Problem 6")
numbers = input("Give me several integers separated by spaces: ")
numbers_list = numbers.split(" ")
sum = 0
for number in numbers_list:
  sum += int(number)
  print(sum)
  break



'''
Problem 7. Add or subtract
You are given a string that starts with either a ‘+’ or a ‘-‘ followed by a space and then
by two integers separated by single spaces.
For example, ‘+ 10 5’ or ‘- 2 100’
Your task is to compute the sum of the integers if the string starts with a ‘+’ or subtract
the 2 nd integer from the 1 st if it starts with a ‘-‘.
Examples:
compute(&#39;+ 10 5&#39;)  15
compute(&#39;- 2 100&#39;)  -98
'''
print("Problem 7")
def compute(expression):
  parts = expression.split(" ")
  if parts[0] == "+":
    return int(parts[1]) + int(parts[2])
  else:
    return int(parts[1]) - int(parts[2])

print(compute("+ 10 5"))
print(compute("- 2 100"))




'''
Problem 8. Same start and end
Ask the user for a string that has several words separated by single spaces. Print all words that start
and end with the same letter (ignoring the case).
Example:
Give me several words separated by spaces: comic bat Apple America baobab
comic
America
baobab
'''
print("Problem 8")
words = input("Give me several words separated by spaces: ")
words_list = words.split(" ")
for word in words_list:
  if word[0].lower() == word[-1].lower():
    print(word)
    break




'''
Problem 9. Biggest number
Write a function with one parameter: a string made of integers separated by single spaces. This
function should return the biggest number.
Examples:
biggest(&#39;20 100 5 35&#39;)  100
biggest(&#39;2 3 10&#39;)  10
'''
print("Problem 9")
def biggest(numbers):
   numbers_list = numbers.split(" ")
   biggest_number = int(numbers_list[0])
   for number in numbers_list:
      if int(number) > biggest_number:
         biggest_number = int(number)
         return biggest_number
         break


print(biggest("20 100 5 35"))
print(biggest("2 3 10"))
print(biggest("100 200 300"))
print(biggest("1 2 3 4 5 6 7 8 9 10"))
print(biggest("10 20 30 40 50 60 70 80 90 100"))
print(biggest("100 200 300 400 500 600 700 800 900 1000"))
print(biggest("1000 2000 3000 4000 5000 6000 7000 8000 9000 10000"))
              









