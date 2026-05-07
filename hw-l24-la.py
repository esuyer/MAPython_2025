icecream = {
  "leon": "mint chocolate chip",
  "lenny": "chocolate",
  "leah": "oreo",
  "ann": "vanilla",
  "marie": "strawberry",
  "pete": "strawberry",
  "kevin": "chocolate",
  "jake": "pistacio",
  "bob": "cookie dough",
  "andre": "mint chocolate chip",
  "ivan": "chocolate",
  "maria": "strawberry",
  "joe": "butter pecan",
  "olivia": "vanilla",
  "papa": "pistacio"
}
print(icecream, "\n")
person = input("give me a person from this list ↑ ")
if person in icecream:
  print(f"{person} likes {icecream[person]} ice cream")
else:
  print(f"who's {person}?")
flavor = input("\nanyways, whats your favorite ice cream? ")
people = []
for key in icecream:
  if flavor == icecream[key]:
    people.append(key)
print(f"{people} is a list of all the people who like the same flavor as you")

