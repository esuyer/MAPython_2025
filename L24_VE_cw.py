#fav_foods={"anna" : "pizza", "leon" : "hotdogs", "luke": "burgers", "ben": "freeze dried burrito", "Vardhan": "pizza", "Marcelo" : "porkchops"}

#num_entries=len(fav_foods)
#print(num_entries)
#yummy=fav_foods["ben"]
#fav_foods["ed"]= "Steak"
#print(fav_foods["ed"])
#fav_foods["luke"]= "Waygu beef"
#del fav_foods["ed"]

#print(fav_foods)


votes_animals={"cat" : 100, "dog" : 150, "rabbit" : 15, "fish" : 20, "pig" :5}

print (votes_animals)

votes_animals["hampster"]= 30
print(votes_animals)

votes_animals["hampster"]= 35

print(votes_animals)

morevotes= int(input("How many new votes did the pig get?"))
votes_animals["pig"]+= morevotes
print(votes_animals)

for key in  votes_animals:
   print(key)

for key in  votes_animals:
   print(votes_animals[key])


for key in votes_animals:
   print(key, "was chosen by", votes_animals[key])

if  "cat" in votes_animals:
  print("this is how many people voted for the cat:",votes_animals["cat"])


print("The total number of votes is", sum(votes_animals.values()))

if votes_animals["cat"]> votes_animals["dog"]:
   print("The cat won by", votes_animals["cat"]- votes_animals["dog"])
else:
   print("The dog won by", votes_animals["dog"]- votes_animals["cat"])

for key in  votes_animals:
   if votes_animals[key]<30:
      print(key, votes_animals[key])


 




