import random

"""
1. Print all integers from 0 to 10 (inclusive).  Use while loop.
"""
print("Problem 1")
i = 0
while i <= 10:
   print(i)
   i += 1

"""
2. Print all integers from 5 to 12 (inclusive).  Use while loop.
"""
print("Problem 2")
i = 5
while i <= 12:
   print(i)
   i += 1



"""
3. Print all integers from 5 to -5 (inclusive) in descending order.  Use while loop.
Expected output:
5
4
3
2
0
-1
-2
-3
-4
-5
"""
print("Problem 3")
i = 5
while i >= -5:
   print(i)
   i -= 1
  

"""
4. Ask the user for an integer less than 50. Print integers from that number to 50 (inclusive) skip
counting by 2.  Use while loop.
Examples:
Give me an integer less than 50: 43
43
45
47
49
Give me an integer less than 50: 46
46
48
50
"""
print("Problem 4")
num = int(input("Give me an integer less than 50: "))
while num <= 50:
   print(num)
   num += 2



"""
5. Ask the user for a positive integer N. Print integers from N to 0 (inclusive) in descending order
skip counting by 3.  Use while loop.
Examples:
Give me a positive integer: 10
10
7
4
1
Give me a positive integer: 6
6
3
0
"""
print("Problem 5")
num = int(input("Give me a positive integer: "))
while num >= 0:
   print(num)
   num -= 3


"""
Problem 6. From a to b
Ask the user for 2 integers: a and b (a &lt; b).
Using while loop, print all integers from a to b. Do not include a but include b.
Example:
Give me an integer: 12
Give me a bigger integer: 17
13
14
15
16
17
"""
print("Problem 6")
a = int(input("Give me an integer: "))
b = int(input("Give me a bigger integer: "))
while a < b:
   a += 1
   print(a)


"""
Problem 7. Loop a list (challenge)
Create a list of words. Print it.
Using while loop, print all words from the list, one per line.
Example:
[&#39;head&#39;, &#39;body&#39;, &#39;tail&#39;]
head
body
tail
Tip: if stuck, start with writing a while loop that prints all valid positions for the list, one per line. Then
modify the code so that instead of positions it prints words from the list at those positions.
"""
print("Problem 7")
words = ["head", "body", "tail"]
i = 0
while i < len(words):
   print(words[i])
   i += 1
  

"""
Problem 8. Loop a list backwards (challenge)
Create a list of words. Print it.
Using while loop, print all words from the list in reversed order, one per line.
Example:
[&#39;head&#39;, &#39;body&#39;, &#39;tail&#39;]
tail
body
head
"""
print("Problem 8")
words = ["head", "body", "tail"]
i = len(words) - 1
while i >= 0:
   print(words[i])
   i -= 1

"""
Squares
Ask the user for a positive integer N.
Using while loop, print the squares of consecutive positive integers (1, 2, 3, …) that are less than N.
For example, for N = 35 the program should print 1, 4, 9, 16, 25. The next square 6 2 = 36 is greater
than 35, so it should not be printed.
Example:
Give me a positive integer: 90
1
4
9
16
25
36
49
64
81
"""
print("Problem 9")
num = int(input("Give me a positive integer: "))
i = 1
while i * i < num:
   print(i * i)
   i += 1


"""
Powers of 2
Ask the user for a positive integer N.
Using while loop, print powers of 2 that are less than N. (Reminder: power of 2 is number 2 raised in
some power. For example, 2 3 ).
For example, for N = 35 the program should print 1, 2, 4, 8, 16, 32. The next square 2 6 = 64 is greater
than 35, so it should not be printed.

Example:
Give me a positive integer: 1000
1
2
4
8
16
32
64
128
256
512
"""
print("Problem 10")
num = int(input("Give me a positive integer: "))
i = 0
while 2 ** i < num:
   print(2 ** i)
   i += 1



"""
Sum
Ask the user for a positive integer N. Add consecutive numbers starting from 1 until the sum becomes
greater than N.
a) Print the sum.
b) Print the last sum that is smaller than N.
c) Print the last number that was included in the sum in b).
Example:
Give me an integer: 50
First sum over the limit: 55
Last sum not over the limit: 45
Last number added: 9
(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45. If we add the next number (10), the sum will be 55 and will exceed the
given limit (50))
Hint: We do not know how many integers we will need to add, so while loop will work well here.
"""
print("Problem 11")
num = int(input("Give me an integer: "))
sum = 0
i = 1
while sum <= num:
   sum += i
   i += 1

print("First sum over the limit:", sum)
print("Last sum not over the limit:", sum - i + 1)
print("Last number added:", i - 2)


"""
Smallest divisor
Given an integer N (N &gt; 1), find its smallest divisor (1 is not a divisor).
Examples:
smallest_div(17)  17
smallest_div(123456)  2
smallest_div(35)  5
"""
print("Problem 12")
def smallest_div(N):
   i = 2
   while i <= N:
      if N % i == 0:
         return i
         break
         #return i

      i += 1

print(smallest_div(123456))  
