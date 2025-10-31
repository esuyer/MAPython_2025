import random
import turtle

turtle.setup(800, 600)
t = turtle.Turtle()

t.width(random.randint(1, 8))

for i in range(4):
  t.forward (50)
  t.left(90)

turtle.done()