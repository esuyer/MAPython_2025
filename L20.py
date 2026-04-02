"""
Problem 1. The bigger the better
Given a list of integers, find out which one is greater, the 1 st element or the last element, and change
all the elements of the list to that value.
Examples:
Before: [1, 2, 3]
After: [3, 3, 3]
Before: [9, 11, 4, 5]
After: [9, 9, 9, 9]
Reminder: use [] notation to change an element of a list.
"""
print ("Problem 1")
num = [9, 11, 4, 5]
if num[0] > num[-1]:
    for i in range(len(num)):
        num[i] = num[0]
else:
    for i in range(len(num)):
        num[i] = num[-1]

print (num)


"""
Problem 2. Bananas
Write a function with 2 parameters: 2 lists of words L1 and L2. This function should change all
words in L1 that appear in L2 to the word “bananas”. Then, it should print L1.
Do not create new lists while solving this problem.
Example:
Function call:
bananas([&quot;donkey&quot;, &quot;apples&quot;, &quot;fly&quot;, &quot;pears&quot;, &quot;moose&quot;], [&quot;moose&quot;, &quot;donkey&quot;, &quot;fly&quot;])
Output:
[&#39;bananas&#39;, &#39;apples&#39;, &#39;bananas&#39;, &#39;pears&#39;, &#39;bananas&#39;]
"""
print ("Problem 2")
def bananas(L1, L2):
    for i in range(len(L1)):
        if L1[i] in L2:
            L1[i] = "bananas"

    print (L1)

bananas(["donkey", "apples", "fly", "pears", "moose"], ["moose", "donkey", "fly"])



"""
Problem 3. Letter triangle
Ask the user for an integer between 1 and 26 (inclusive). Print the pattern of letters like in the
examples below:
Examples:
Give me an integer between 1 and 26: 5
A
BB
CCC
DDDD
EEEEE
Give me an integer between 1 and 26: 3
A
BB
CCC
Tip: if stuck, think how we could store the letters so we could access them in order.
"""
print ("Problem 3")
num = int(input("Give me an integer between 1 and 26: "))
for i in range(1, num+1):
    print (chr(64+i)*i)




"""
Problem 4. Potion brewing
Wizard Mizgog brews invisibility potion in his cauldron. He wants to empty his cauldron into
12-oz vials. Mizgog wants to know the smallest number of vials he will need to empty his
cauldron.
Write a program that asks how many ounces of invisibility potion Mizgog brewed.
The program should calculate and print the smallest number of vials Mizgog will need.
Do not use operators //, /, % while solving this problem. Use while loop.
Examples:
How many ounces of potion do you have? 36
You need 3 12-oz vials
How many ounces of potion do you have? 15
You need 2 12-oz vials
"""
print ("Problem 4")
ounces = int(input("How many ounces of potion do you have? "))
vials = 0
while ounces > 0:
    ounces -= 12
    vials += 1

print ("You need", vials, "12-oz vials")


"""
Problem 5. Just the digits
Write a function with 1 parameter: a string S.
It should create and return a new string made only of the digits from S (in the same order they
appear in S). (The digits here are the characters “0”, “1”, …, “9”)
Examples:
just_digits(&quot;12 + 34 = 46&quot;)  &quot;123446&quot;
just_digits(&quot;5 rubies, 10 emeralds, 4 moonstones&quot;)  &quot;5104&quot;
"""
print ("Problem 5")
def just_digits(S):
    new_string = ""
    for i in S:
        if i.isdigit():
            new_string += i

    return new_string

print (just_digits("12 + 34 = 46"))


"""
Problem 6. The circle of letters
Ask the user for a word. Using this word, print the pattern like the one in the example below:
Example:
Give me a word: python
python
npytho
onpyth
honpyt
thonpy
ythonp
Tip: slicing could be helpful here.
"""
print ("Problem 6")
word = input("Give me a word: ")
for i in range(len(word)):
    print (word[i:] + word[:i])




"""
Problem 7. Make a word
Write a function with 1 parameter: a list of words. This function should create and return a string
made of the first letters of the words in this list.
Examples:
print(from_first([&#39;hive&#39;, &#39;emu&#39;, &#39;life&#39;, &#39;lime&#39;, &#39;open&#39;]))  &#39;hello&#39;
print(from_first([&#39;win&#39;, &#39;one&#39;, &#39;wolf&#39;]))  &#39;wow&#39;
"""
print ("Problem 7")
def from_first(words):
    new_string = ""
    for i in words:
        new_string += i[0]

    return new_string

print (from_first(['hive', 'emu', 'life', 'lime', 'open']))


"""
Problem 8. Interesting words
We will consider a word “interesting” if it satisfies at least one of the following:
 it is the word “interesting” (in any combination of upper and lowercase letters)
 it contains both letters “x” and “y” (ignoring the case)
 it starts and ends with the same letter
Write a function with 1 parameter: a word. It should return True if the word is “interesting” and False
otherwise.
Examples:
is_interesting(&#39;INTEREsting&#39;)  True
is_interesting(&#39;Madam&#39;)  True
is_interesting(&#39;Sir&#39;)  False
is_interesting(&#39;Xylophone&#39;)  True
is_interesting(&#39;Box&#39;)  False
is_interesting(&#39;Yay&#39;)  True
"""
print ("Problem 8")
def is_interesting(word):
   if word.lower() == "interesting":  
      return True  
   elif "x" in word.lower() and "y" in word.lower():
      return True
   elif word[0].lower() == word[-1].lower():
      return True
   else:
      return False

print (is_interesting("INTEREsting"))
print (is_interesting("Madam"))
print (is_interesting("Sir"))
print (is_interesting("Xylophone"))
print (is_interesting("Box"))
print (is_interesting("Yay"))
print (is_interesting("Xy"))
print (is_interesting("xy"))
print (is_interesting("XyX"))
print (is_interesting("XyY"))

     



