def make_mouse():
  animal = "mouse"
  print (animal)

def make_beaver():
  global animal
  animal = "beaver"
  print (animal)

def make_cow():
  print ("old value of animal is", animals)
  animal = "cow"
  print ("new value of animal is", animal)



animal = "horse"
animals = ["cat", "dog", "fish"]

make_mouse()  # mouse
make_beaver() # beaver
make_cow()
print(animal)

# print 1: mouse
# print 2: beaver
# print 3: beaver
# print 4: old value is:
# print 4: new value is: