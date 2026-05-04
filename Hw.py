print("Problem 1\n")
flavor = {"Marie":"Vanilla",
          "Pete":"Chocolate",
          "Kevin":"Strawberry",
          "Ann":"Blueberry",
          "Jake":"Rasberry"}
scores = {"Marie":135,
          "Pete":150,
          "Kevin":120,
          "Ann":100}
print(scores)
scores["Marie"] = 120
scores["Jake"] = 105
scores["Kevin"] = scores["Kevin"] + 10
print(scores)

print("\nProblem 2\n")
a = input("Enter a name: ")
if a in flavor:
  print(a, "favorite ice cream flavor is ", flavor[a])
else:
  print("No information is avalible for that name.")
b = input("What's your favorite flavor? ")
for a in flavor:
  if b in flavor[a]:
    c = 0
    c = c + 1
print("Number of people that like", b, " ice cream: ", c)

print("\nProblem 3\n")
place = people = {
  "Andre": "France",
  "Jake": "USA",
  "Ivan": "Russia",
  "Maria": "Canada",
  "Pete": "USA"}
d = input("Which country do you live in? ")
print("People who also live in ", d)
for a in place:
  if d in place[a]:
    print(a)

print("\n Problem 4\n")
def test_passed(w, x, y, z):
  total = w + x + y + z
  if total < 360:
      return False
  else:
      return True
print(test_passed(100, 95, 90, 90)) 
print(test_passed(100, 85, 100, 100))
print(test_passed(90, 90, 89, 90))
print(test_passed(90, 90, 90, 90))

print("\nProblem 5\n")
years = {'Joe': 1, 'Kevin': 99, 'Annie': 30, 'Pete': 15} 
x = int(input("How many years have passed?"))
print(x, "years passed: ")
for key in  years:
  years[key] = years[key] + x
print(years)