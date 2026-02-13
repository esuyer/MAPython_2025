import time
import random
def a_an(word):
  if word[0] == "a" or  word[0] == "e" or  word[0] == "i" or  word[0] == "o" or  word[0] == "u" or  word[0] == "h":
    return f"an {word}"
  else: 
    return f"a {word}"
colors = ["green", "blue", "orange", "teal or turquoise", "purple", "cyan", "black", "white", "maroon", "indigo", "red", "grey", "yellow", "pink", "magenta", "brown", "beige", "periwinkle", "rainbow"]
nouns = ["dog", "sock", "cat", "castor canadensis", "bike", "cheese", "phone", "chicken nugget", "waffle", "pancake", "parrot", "frog", "log", "pillow", "penguin", "poop"]
adjs = ["fluffy", "yummy", "smelly", "just like Lenny", "jumpy", "loud", "quiet", "stinky", "cheesy", "happy", "sad", "wierd", "delicious", "broken", "rough", "smooth", "colorful", "bland"]
for i in range(random.randint(4, 10)):
  print(f"i got {a_an(colors[random.randint(0,colors.__len__()-1)])} {nouns[random.randint(0,nouns.__len__()-1)]} for new years. it was {adjs[random.randint(0,adjs.__len__()-1)]}")
