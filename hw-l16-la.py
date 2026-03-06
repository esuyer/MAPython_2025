word = input("give me a word: ")
word.lower()
if word.lower()[0] == word.lower()[-1]:
  print(word, "starts and ends with", word.lower()[0])
else:
  print(word, "does not start and end with the same letter")
print("now im gonna yell it at your face,", word.upper())

print("next")

word1 = input("give me a single character: ")
word2 = input("give me another single charcter: ")
if word1 > word2:
  print(f"{word1} comes after {word2} in python")
elif word1 == word2:
  print("thats the same letter")
else:
  print(f"{word1} comes before {word2} in python")

print("next")

def voweltoplus(word = ""):
  newword = ""
  for i in range(word.__len__()):
    if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u" or word[i] == "A" or word[i] == "E" or word[i] == "I" or word[i] == "O" or word[i] == "U":
      newword += "+"
    else:
      newword += word[i]
  return newword

word = input("give me a word")
print("heres the own word but vowels are +:", voweltoplus(word))
