import turtle 
import random
num_spirals = 4
for i in range(num_spirals):
   t = turtle.Turtle()
   t.speed(0)
   t.pensize(2)
   t.color(random.random(), random.random(), random.random())
   for j in range(100):
       t.forward(j * 2)
       t.left(90)