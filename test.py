import turtle 
import random
num_spirals = 4
pens = []
for i in range(num_spirals):
   p= turtle.Pen()
   p.color("green")
   p.pensize(2)
   pens.append(p)
for p in pens:
   p.forward(100)  













turtle.done