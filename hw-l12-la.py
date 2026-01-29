import time
word = input("give me a word: ")
print("here are all the a's in", word + ":")
time.sleep(1)
for i in word:
  if i == "a" or i == "A":
    print(i)
    time.sleep(0.5)
  else:
    print(".")
    time.sleep(0.1)
time.sleep(1.5)
print("next")
word1 = input("give me a word: ")
word2 = input("give me another word: ")
if word1[-1] == word2[0]:
  print(word1, "and", word2, "can form the chain:", word1[:-1] + word2)
elif word2[-1] == word1[0]:
    print(word1, "and", word2, "can form the chain:", word2[:-1] + word1)
else:
  print(word1, "and", word2, "cannot form a chain")
time.sleep(2)
print("next")
time.sleep(1)
word1 = input("give me a word: ")
word2 = input("give me another word: ")
if word1[-2:-1] == word2[-2:-1]:
  print(word1, "and", word2, "rhyme")
else:
  print(word1, "and", word2, "do not rhyme")
