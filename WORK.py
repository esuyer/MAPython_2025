def make_mosue():
  animal = "mouse"  #local variable
  print(animal)

def make_beaver():
  global animal
  animal = "beaver" #global variable
  print(animal)

def make_cow():
  print("Old value of animal is", animal)
  animal = "cow" #local variable
  print("New value of animal is", animal)


animal = "horse" #global variable
make_mosue() #mouse
make_beaver() #beaver
make_cow() #cow
print(animal)#horse
