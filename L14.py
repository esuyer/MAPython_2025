fruit = ['apple', 'banana', 'cherry', 'apple', 'apple']
if  "apple" in fruit:
  print("Yes, 'apple' is in the fruits list")

if "blueberry" in fruit:
  ind = fruit.index('blueberry')
  print("fruit is at index", ind)
else:
  print("fruit not in list")

count = fruit.count('apple')

print(count)

fruit.append('blueberry')
fruit.append('mango')

print("before ", fruit)
fruit.insert(0, 'tomato')
print("after ", fruit)

fruit.remove('tomato')
print("after remove ", fruit)

