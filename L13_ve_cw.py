wishlist= ["iphone","Samsung","ipad","macbook"]
print(wishlist)

int= [1,2,3,4,5]
print(int)

stuff= ["iphone",1,2,3,"ipad"]
print(stuff)


friend=[]
friend.append("Bob")
friend.append("Mary")
friend.append("John")
print(friend)


print(len(friend))
print(friend[0])

del wishlist[1]

if "John" in friend:
   print("John is in the list")



for i in range(len(friend)):
   print(friend[i])

favcolors=["red","blue","green","yellow"]
print("First:",favcolors[0])
print("Last:",favcolors[-1])

if "Magenta" in favcolors:
   print("Magenta is in the list")
else:
   print("Magenta is not in the list")

for i in range(len(favcolors)):
   print(i + 1, ":", favcolors[i])