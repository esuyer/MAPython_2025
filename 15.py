import turtle
import random

num_spirals = 8
directon = 0

pens = []
for i in range(num_spirals):
  p = turtle.Pen()
  p.color("green")
  p.pensize(2)
  directon = directon + 360 / num_spirals
  p.setheading(directon)
  pens.append(p)


for p in pens:
  for i in range(100, 0, -1):
    p.forward(i)
    p.right(100)



# Keep the window open
turtle.done()
