import turtle
import random


t = turtle.Turtle()
t.speed(5)
for i in range(5):
    side = random.randint(50, 200)
    for j in range(3):
        t.forward(side)
        t.left(120)
    t.penup()
    t.forward(side + 20)
    t.pendown()
turtle.done()
