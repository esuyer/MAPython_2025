"""
Problem 1. Find “Python”
Create a list of words. Print it.
Check if the word “Python” is there. If so, print its index (use function index). Otherwise, print
“Python not found”.
Examples:
[&#39;Java&#39;, &#39;Scratch&#39;, &#39;Python&#39;, &#39;C++&#39;]
Found Python at index 2
[&#39;cat&#39;, &#39;dog&#39;, &#39;table&#39;]
Python not found
"""
print ("Problem 1")
print ("-----------")

words = ['Java', 'Scratch', 'Python', 'C++']
if "Python" in words:
  ind = words.index('Python')
  print("Found Python at index", ind)
else:
  print("Python not found")
  

"""
Problem 2. Test grades
Use function count to solve this problem.
Create a list of letters – grades from A to D that a group of students received on a test (one grade per
student). Print the list.
a) Print how many As were received
b) Print how many Bs were received
c) The teacher said that those who received a C or a D could retake the test. How many people
can retake the test?
Example:
[&#39;A&#39;, &#39;C&#39;, &#39;D&#39;, &#39;C&#39;, &#39;B&#39;, &#39;B&#39;, &#39;A&#39;, &#39;A&#39;]
Got A: 3
Got B: 2
Can retake: 3
"""
print ("Problem 2")
print ("-----------")
grades = ['A', 'C', 'D', 'C', 'B', 'B', 'A', 'A']
print("Got A:", grades.count('A'))
print("Got B:", grades.count('B'))
print("Can retake:", grades.count('C') + grades.count('D'))




"""
Problem 3. Beginning, middle, end
Create a list of words. Print it.
Do the following (in this order):
a) Add the word “beginning” to the beginning of the list.
b) Add the word “end” at the end of the list.
c) If the list has an even number of words, insert the word “middle” in the middle of the list. If the
list has an odd number of words, do nothing.
Print the list.
Test your program with lists that have an even and odd number of words.
Examples:
Before: [&#39;cat&#39;, &#39;dog&#39;, &#39;book&#39;, &#39;table&#39;]
After: [&#39;beginning&#39;, &#39;cat&#39;, &#39;dog&#39;, &#39;middle&#39;, &#39;book&#39;, &#39;table&#39;, &#39;end&#39;]
Before: [&#39;cat&#39;, &#39;dog&#39;, &#39;book&#39;]
After: [&#39;beginning&#39;, &#39;cat&#39;, &#39;dog&#39;, &#39;book&#39;, &#39;end&#39;]
"""
print ("Problem 3")
print ("-----------")
words = ['cat', 'dog', 'book', 'table']
words.insert(0, 'beginning')
words.append('end')
if len(words) % 2 == 0:
  words.insert(len(words)//2, 'middle')

print(words)


"""
Problem 4. Ticket line
Jenna and Andrew are standing in line for movie tickets. Given a list of people’s names in order they
stand in line, do the following:
a) Print Jenna’s and Andrew’s positions in line (positions starting with 1).
b) Print how many people are in front of Jenna
c) Print how many people are behind Andrew.
You can assume that there is only one Jenna and only one Andrew in line.
Example:
[&#39;Sam&#39;, &#39;Jenna&#39;, &#39;Max&#39;, &#39;Andrew&#39;, &#39;Grace&#39;, &#39;Bob&#39;]
Jenna pos: 2
Andrew pos: 4
There are 1 people in front of Jenna
There are 2 people behind Andrew
"""
print ("Problem 4")
print ("-----------")
names = ['Sam', 'Jenna', 'Max', 'Andrew', 'Grace', 'Bob']
print("Jenna pos:", names.index('Jenna') + 1)
print("Andrew pos:", names.index('Andrew') + 1)
print("There are", names.index('Jenna'), "people in front of Jenna")
print("There are", len(names) - names.index('Andrew') - 1, "people behind Andrew")




"""
Problem 6. Squares
Given a list of numbers, create a new list that contains the squares of the numbers from the original
list.
Example:
Original list: [-3, 10, 16, -2, 19]
New list: [9, 100, 256, 4, 361]
Tip: the new list should start empty.
"""
print ("Problem 6")
print ("-----------")
numbers = [-3, 10, 16, -2, 19]
squares = []
for i in range(len(numbers)):
  squares.append(numbers[i] ** 2)

print(squares)



"""
Problem 7. Player replacement
Several people are playing beach volleyball on the beach. Kevin had to go home, and
Jake replaced him.
You are given a list of the names of the players. There is one Kevin among them.
Print the list. Change &#39;Kevin&#39; to &#39;Jake&#39; and print the list again.
Solve this problem without loops. Think which of the functions we learned can be useful here.
Examples:
Before: [&#39;Ann&#39;, &#39;Sam&#39;, &#39;Kevin&#39;, &#39;Bob&#39;]
After replacement: [&#39;Ann&#39;, &#39;Sam&#39;, &#39;Jake&#39;, &#39;Bob&#39;]
Before: [&#39;Kevin&#39;, &#39;Bob&#39;, &#39;Mary&#39;, &#39;George&#39;, &#39;Jenna&#39;]
After replacement: [&#39;Jake&#39;, &#39;Bob&#39;, &#39;Mary&#39;, &#39;George&#39;, &#39;Jenna&#39;]
"""
print ("Problem 7")
print ("-----------")
players = ['Ann', 'Sam', 'Kevin', 'Bob']
print("Before:", players)
ind = players.index('Kevin')
players[ind] = 'Jake'
print("After replacement:", players)
  


"""
Problem 8. Reversed list
Given a list, create a new list made of the elements of the given list in reverse order. The original list
should remain unchanged.
Examples:
Original: [&#39;cat&#39;, &#39;dog&#39;, &#39;fish&#39;, &#39;hamster&#39;]
New list: [&#39;hamster&#39;, &#39;fish&#39;, &#39;dog&#39;, &#39;cat&#39;]
Original: [1, 2, 3, 4, 5]
New list: [5, 4, 3, 2, 1]

"""
print ("Problem 8")
print ("-----------")

original  = [1, 2, 3, 4, 5]
new_list = []
for i in range(len(original)):
   new_list.append(original[len(original) - i - 1])

print(new_list)
print(original)

"""
Find the mouse
You are given a list of words of even length. There might be a single word “mouse” hiding in it.
If it’s there, print its position and whether it’s in the 1 st half of the list or in the 2 nd . Otherwise, print
“Mouse not found”
Examples:
[&#39;book&#39;, &#39;cat&#39;, &#39;mouse&#39;, &#39;dog&#39;]
Found mouse at position 2
In the 2nd half
[&#39;mouse&#39;, &#39;window&#39;, &#39;cat&#39;, &#39;door&#39;, &#39;table&#39;, &#39;sofa&#39;]
Found mouse at position 0
In the 1st half
Test you program for the following lists:
 A list where the word “mouse” is in the first half of the list
 A list where the word “mouse” is in the second half of the list
 A list that does not have the word “mouse”.
Hint: what are the indices of the words in the first half of the list? What can you tell about them in
relation to the length of the list?
"""
print ("Problem 9")
print ("-----------")
words = ['mouse', 'window', 'cat', 'door', 'table', 'sofa']
if "mouse" in words:
  ind = words.index('mouse')
  print("Found mouse at position", ind)
  if ind < len(words) // 2:
    print("In the 1st half")
  else:
    print("In the 2nd half")    
else:
  print("Mouse not found")



"""
Rotate a list
Given a list, rotate it 1 position to the right:
The 1 st element should become the 2 nd , the 2 nd – the 3 rd , …, the last one should become the 1 st one.
For this problem you are not allowed to use loops. Think which functions that we learned will be
useful here.
def rotate_1right (my_list):
Examples:
rotate_1right([3, 99, 164])  [164, 3, 99]
rotate_1right([32])  [32]
rotate_1right([])  []

"""
print ("Problem 10")
print ("-----------")
def rotate_1right (my_list):
   if len(my_list) > 0:
      my_list.insert(0, my_list.pop())
      return my_list
      #return my_list[-1:] + my_list[:-1]
   else:
      return my_list

print(rotate_1right([3, 99, 164]))
print(rotate_1right([32]))
print(rotate_1right([]))
print(rotate_1right([1, 2, 3, 4, 5]))
print(rotate_1right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(rotate_1right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
print(rotate_1right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
print(rotate_1right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))








