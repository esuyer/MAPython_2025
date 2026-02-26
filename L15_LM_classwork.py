import turtle
import random

num_sprials = 4
direction = 0

pens = []
for i in range(num_sprials):
   p =  turtle.Pen()
   p.color("green")
   p.pensize(2)
   pens.append(p)
   direction = direction + 360/ num_sprials
   p.setheading(direction)

for p in  pens:
   for i in range(100, 0, -1):
      p.forward(i)
      p.right(25)
   
turtle.done() 