"""
Problem 1. Sum of positive numbers
Given a list of numbers, compute and print the sum of all positive numbers.
Example:
[10, -50, 1000, -7, -999, 700]  1710
"""
print ("Problem 1")
num = [10, -50, 1000, -7, -999, 700]
sum = 0
for i in num:
    if i > 0:
        sum += i
        
      
print (sum)
print ("The sum of all positive numbers is", sum)



"""
Problem 2. Multiple of 7
Given a list of numbers, check if there is a multiple of 7 in this list. Print the result (True/False).
Examples:
[10, 0, 1000, -14, -999, 700]  True
[5, -10, 8]  False
"""
print ("Problem 2")
num = [10, 0, 1000, -14, -999, 700]
for i in num:
    if i % 7 == 0:
        print (True)
        break
      

"""
Problem 3. Smallest number
Rewrite the algorithm for finding the biggest number in a list so that it finds and prints the smallest
number in the list.
Use function min to check your answer.
Examples:
Input Output
[3, 1, -10, 17] My algorithm:-10
Function min: -10
[100, 33, 40, 6, 1] My algorithm: 1
Function min: 1
"""
print ("Problem 3")
num = [3, 1, -10, 17]
smallest = num[0]
for i in num:
    if i < smallest:
        smallest = i


print ("Function min:", smallest)




"""
Problem 4. Start with leprint ("Problem 1")tter ‘a’
Given a list of words in all lowercase letters, count and print how many words start with the letter ‘a’.
Examples:
[&#39;avocado&#39;, &#39;cat&#39;, &#39;at&#39;, &#39;archer&#39;, &#39;zebras&#39;]  3
[&#39;buzz&#39;, &#39;land&#39;, &#39;fly]  0
"""
print ("Problem 4")
words = ['avocado', 'cat', 'at', 'archer', 'zebras']
count = 0
for i in words:
    if i[0] == 'a':
        count += 1

print (count)



"""
Problem 5. Length of longest word
Modify the algorithm for finding the biggest element so it finds the length of the longest word instead
(search for biggest length).
Example:
[&#39;buzz&#39;, &#39;Python&#39;, &#39;cat&#39;, &#39;at&#39;, &#39;zebras&#39;]
The longest word has 6 letters
Tip: Here, you will need to compare lengths of the words instead of the elements in the list.
"""
print ("Problem 5")
words = ['buzz', 'Python', 'cat', 'at', 'zebras']
longest = len(words[0])
for i in words:
    if len(i) > longest:
        longest = len(i)

print ("The longest word has", longest, "letters")



"""
Problem 6. Longest word
Rewrite your solution for problem 2 so it also prints the longest word. If there are several words that
are tied for being the longest, print the first one.
Example:
[&#39;buzz&#39;, &#39;python&#39;, &#39;cat&#39;, &#39;zebras&#39;]
The longest word has 6 letters: python
"""
print ("Problem 6")
words = ['buzz', 'python', 'cat', 'zebras']
longest = len(words[0])
for i in words:
    if len(i) > longest:
        longest = len(i)
        longest_word = i

print ("The longest word has", longest, "letters:", longest_word)


"""
Problem 7. Function find
Implement function find for lists. It should have 2 parameters: a list and a value. This function should
return the index of the first occurrence of the value in the list. If the value is not in the list, it should
return -1.
Do not use function index. Write your own algorithm.
Examples:
find([&#39;dog&#39;, &#39;python&#39;, &#39;cat&#39;, &#39;zebra&#39;, &#39;cat&#39;, &#39;mouse&#39;], &#39;cat&#39;)  2
find([1, 5, 10, 4], 7)  -1
"""
print ("Problem 7")
def find(list, value):
    for i in range(len(list)):
        if list[i] == value:
            return i

    return -1

print (find(['dog', 'python', 'cat', 'zebra', 'cat', 'mouse'], 'cat'))



"""
Problem 8. Function right_find
Implement function right_find for lists. It should have 2 parameters: a list and a value. This function
should return the index of the last occurrence of the value in the list (it should start searching the list
from the right). If the value is not in the list, it should return -1.
Do not use function index. Write your own algorithm.
Examples:
right_find([&#39;dog&#39;, &#39;python&#39;, &#39;cat&#39;, &#39;zebra&#39;, &#39;cat&#39;, &#39;mouse&#39;], &#39;cat&#39;)  4
right_find([1, 5, 10, 4], 7)  -1
"""
print ("Problem 8")
def right_find(list, value):
   for i in range(len(list)-1, -1, -1):
      if list[i] == value:
         return i
         break

   return -1
  
   print (right_find(['dog', 'python', 'cat', 'zebra', 'cat', 'mouse'], 'cat'))
   print (right_find([1, 5, 10, 4], 7))
   print (right_find([1, 5, 10, 4], 10))
  