"""
Solve ALL problems in the same file.
A poll was conducted about people’s favorite pets. The following information was collected:
Favorite animal Number of votes
cat 100
dog 150
rabbit 15
fish 20
pig 5
Create a poll dictionary with the following pairs:
key – pet type (a string),
value – number of people who liked that pet (an integer).
This dictionary should store the information from the table above.
1. Print the whole dictionary.
2. Using [] notation add another pair to the dictionary: &#39;hamster&#39; that was liked by 30 people.
Print the dictionary.
3. Using [] notation change the value for &#39;hamster&#39; to 35. Print the dictionary.
4. Ask the user: &#39;How many new votes did the pig get?&#39; Use [] notation to change the
value connected to the key &#39;pig&#39; by adding the new votes. Print the dictionary.
Example:
How many new votes did the pig get? 3
{&#39;cat&#39;: 100, &#39;dog&#39;: 150, &#39;rabbit&#39;: 15, &#39;fish&#39;: 20, &#39;pig&#39;: 8, &#39;hamster&#39;: 35}
5. Loop through the dictionary and print just the keys, one key per line
Output:
cat
dog
rabbit
fish
pig
hamster
6. Loop through the dictionary and print just the values, one value per line
Output:
100
150
15
20
8
35


7. Loop through the dictionary and print both the keys and the values, one pair per line using the
format below

Output:
cat was chosen by 100 people
dog was chosen by 150 people
rabbit was chosen by 15 people
fish was chosen by 20 people
pig was chosen by 8 people
hamster was chosen by 35 people
8. Check if a cat is in the dictionary. If it is, print how many people liked it in format:
“___ people chose cat as their favorite animal”
9. Calculate how many people took part in the poll.
Tip: add all the values together.

10. Compare the number of people that chose a dog to the number of people that chose a cat.
Print which animal was liked more: dog or cat. By how much?
11. Print which animals were chosen by less than 30 people.
Output:
rabbit 15
fish 20
pig 8

"""
print ("problem 1")
poll = {"cat" : 100, "dog" : 150, "rabbit" : 15, "fish" : 20, "pig" : 5}
print (poll)
poll["hamster"] = 30
print (poll)
poll["hamster"] = 35
print (poll)
new_votes = int(input("How many new votes did the pig get? "))
poll["pig"] += new_votes
print (poll)

total = 0
dog_votes = 0
cat_votes = 0

for key in poll:
    print (key)
    print (poll[key])
    print (key, "was chosen by", poll[key], "people")
    if key == "cat":
        print (poll[key], "people chose cat as their favorite animal")
    total += poll[key]
    if key == "dog":
        dog_votes = poll[key]
    if key == "cat":
        cat_votes = poll[key]
    if poll[key] < 30:
        print (key, poll[key])

for key in poll:
    total += poll[key]
print (total)
if dog_votes > cat_votes:
    print ("dog was liked more than cat by", dog_votes - cat_votes)
else:
    print ("cat was liked more than dog by", cat_votes - dog_votes)
for key in poll:
    if poll[key] < 30:
        print (key, poll[key])
