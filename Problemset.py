import random
print("Question 3\n")
n = int(input("Give me an integer between 1 and 26: "))
if 1 <= n <= 26:
  for i in range(n):
   letter = chr(65 + i)
   count = 1
   print(letter * (i + count))
   count+=1
print("\nQuestion 6\n")
word = input("Give me a word: ")

for i in range(len(word)):
    print(word[i:] + word[:i])