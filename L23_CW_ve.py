

#def make_mouse():
#  animal="mouse"
#  #local variable
#  print(animal)

#def make_beaver():
#  global animal
#  animal="beaver"
#  print(animal)

#def make_cow():
#  print("old value of animal is", animal)
#  animal="cow"
#  print("new value of animal is", animal)

#animals = ["cat", "dog", "fish"]
  

#animal="horse"
#make_mouse()
#make_beaver()
#global variable
#print(animal)


import turtle


#def count(x, y):
#global counter
#counter += 1
#    p.clear()
#    p.write("Counter: " + str(counter), font=("Calibri", 15, "normal"))


turtle.setup(600, 400)
p = turtle.Pen()
Colors= ['green', 'red', 'blue']
index=0



def make_circle(x,y):
  global index
  p.color(Colors[index])
  index = (index + 1) % len(Colors)
  p.begin_fill()
  p.circle(50)
  p.end_fill()

#counter = 0
#p.clear()
#p.write("Counter: " + str(counter), font=("Calibri", 15, "normal"))

turtle.onscreenclick(make_circle,1)


turtle.mainloop()