word=input("Enter a word with at least 2 letters: ")
print("The length of the word is:",len(word))
print("The first letter is:",word[0])
print("The last letter is:",word[len(word)-1])

word2=input("Enter a word: ")
if word2[0]==word2[len(word2)-1]:
  print("The first and last letters are",word2[0])
else:
  print("The first and last letters are not the same")