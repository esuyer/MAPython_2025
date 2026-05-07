print("-----------------")
print(" problem 1 ")
print("-----------------")
test_scores={"Marie": 135, "Pete": 150, "Kevin": 120, "Ann": 100}
print(test_scores)
test_scores["Marie"]=120
test_scores["Jake"]=105
test_scores["Kevin"]+=10
print(test_scores)

print("-----------------")
print(" problem 2 ")
print("-----------------")
fav_icecream={"Anna": "chocolate", "Ben": "vanilla", "Luke": "strawberry", "Vardhan": "mint", "Marcelo": "vanilla", "Bob" : "fudge"}
print(fav_icecream)
name= input("What is your name?")
if name in fav_icecream:
   print("Your favorite icecream is", fav_icecream[name])
else:
  print("We do not know which ice cream",name,"likes")
  
