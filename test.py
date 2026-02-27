import turtle 
import random
num_spirals = 36
direction=0
pens = []
for i in range(num_spirals):
   p= turtle.Pen()
   p.color("green")
   p.pensize(2)
   direction = direction + 360 / num_spirals
   print(direction)
   p.setheading(direction)
   pens.append(p)


for p in pens:
   for i in range(10):
      p.forward(i)
      p.right(10)
      p.forward(i)
      p.left(10)
      p.backward(i)

turtle.done()