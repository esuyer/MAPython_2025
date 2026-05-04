pets= {"Cat": 100,
      "Dog":150,
      "Rabbit":15,
      "Fish":10,
      "Pig":5}
print(pets)
pets["Hampster"] = 35
print(pets)
a = int(input("How many more votes did the pig get?: "))
pets["Pig"] = pets["Pig"] + a
print(pets)
for key in pets:
  print(key)
for key in pets:
  print(pets[key])
for key in pets:
  print(key, " was chosen by ", pets[key]," people.")
for key in pets:
  if key == "Cat":
    print(pets[key], " people chose cat as thier favorite animal.")
b = pets["Cat"]
c = pets["Dog"]
d = pets["Rabbit"]
e = pets["Fish"]
f = pets["Pig"]
g = pets["Hampster"]
print("The total people who voted is ", int(b) + int(c) + int(d) + int(e) + int(f) + int(g),)
h = pets["Dog"]
i = pets["Cat"]
if  int(h) > int(i):
  print("The dog is the favorite animal by ", int(h) - int(i), " people.")
else:
   print("The cat is the favorite animal by ", int(i) - int(h), " people.")
for key in pets:
   if pets[key] < 30:
      print(key, pets[key])