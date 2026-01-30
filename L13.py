# how to declare a list with some items
wishlist = ['iphone', 'samsung', 'macbook', 'dell', 'lenovo']
print(wishlist)

ints = [1, 2, 3, 4, 5]
print(ints)

stuff = ['iphone', 1, 'samsung', 2, 'macbook', 3, 'dell', 4, 'lenovo', 5]
print(stuff)

# how to decleare an empty list and append items
friend = []
friend.append('John')
friend.append('Mary')
friend.append('Bob')
print(friend)

print(len(friend))
print(friend[0])

# how to remove an item from a list
del wishlist[1]
print(wishlist)

# how to check if an item is in a list
if "John" in friend:
   print("John is in the list")

# how to loop through a list
for i in range(len(friend)):
   print(friend[i])


