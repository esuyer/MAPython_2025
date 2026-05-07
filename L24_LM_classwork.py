print("Question 1\n")
dictionary  = {"cat": 100, "dog": 150, "rabbit": 15, "fish": 20, "pig": 5}
print(dictionary)
print("\nQuestion 2\n")
dictionary["hamster"] = 30
print(dictionary)
print("\nQuestion 3\n")
dictionary["hamster"]=35
print(dictionary)
print("\nQuestion 4\n")
pig_vote= int(input("How many new votes should the pig get?"))
dictionary["pig"] += int(pig_vote)
print(dictionary)
print("\nQuestion 5\n")
for key in dictionary:
    print(key)
print("\nQuestion 6\n")
for key in dictionary:
  value=dictionary[key]
  print(value)
print("\nQuestion 7\n")
for key in dictionary:
  value=dictionary[key]
  print(key,"was chosen by",value)
print("\nQuestion 8\n")
if "cat" in dictionary:
  value=dictionary[key]
  print(dictionary["cat"],"people voted for the cat")
print("\nQuestion 9\n")
total=sum(dictionary.values())
print(total,"people voted on this poll")
print("\nQuestion 10\n")
if dictionary["dog"]>dictionary["cat"]:
  print("more people voted for the dog by", dictionary["dog"]-dictionary["cat"])
else:
  print("more people vited for the cat by", dictionary["cat"]-dictionary["dog"])
print("\nQuestion 11\n")
threshold = 30
low_vote = [key for key, value in dictionary.items() if value < threshold]
print(low_vote)