print("Question 1\n")
words = ["hello", "world", "python", "jam"]
def make_pairs(words):
  new_list = []
  for word in words:
      new_list.append(word)
      new_list.append(word)
  print(new_list)
make_pairs(words)
print("\nQuestion 2\n")
L = [12, 33, 44, 55, 66, 77, 88, 99]
def get_symmetrical(L):
  new_list = []
  for num in L:
      tens = num // 10
      ones = num % 10
      if tens == ones:
          new_list.append(num)
  print(new_list)
get_symmetrical(L)
print("\nQuestion 3\n")
def sandwich(words):
  index = words.index("jam")
  if index > 0 and index < len(words) - 1 and words[index - 1] == "bread" and words[index + 1] == "bread":
      print("We have a jam sandwich!")
  else:
      print("Missing some bread for a proper sandwich.")
sandwich(words)
print("\nQuestion 4\n")
bob_list = ["curling", "hockey", "bobsledding", "skating"]
joe_list = ["hockey", "skating", "bobsledding", "curling"]
def winter_games(bob_list, joe_list):
  new_list = []
  for game in bob_list:
      if game in joe_list:
          new_list.append(game)
  print(new_list)
winter_games(bob_list, joe_list)
print("\nQuestion 5\n")
print("Sooo, my turtle still doesn't work so I couldn't so this one.")
print("\nQuestion 6\n")
def make_symmetrical(L):
  length = len(L)
  for i in range(length // 2):
      L[i] = L[length - 1 - i]
  print(L)
make_symmetrical(L)