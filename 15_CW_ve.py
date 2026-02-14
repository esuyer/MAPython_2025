import turtle
import random

num_spirals = 4
dirrection=0

pens = []
for i in range(num_spirals):
  p = turtle.Pen()
  p.color("green")
  p.pensize(2)
  dirrection= dirrection + 360 / num_spirals
  p.setheading(dirrection)
  pens.append(p)

for p in pens:
  for i in range(100, 0, -1):
    p.forward(i)
    p.forward(10)


turtle.done()
