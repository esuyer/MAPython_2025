import turtle
import random

turtle.setup(600, 400)
turtle.tracer(3)


##num_spirals = 8
num_spirals = 8

direction = 0
pens = []
for i in range(num_spirals):
    pen = turtle.Pen()
    pen.color(random.random(), random.random(), random.random())
    pen.setheading(direction)
    # pen.color("green")
    pen.pensize(2)
    pen.speed(0)

    pens.append(pen)
    direction = direction + 360 / num_spirals
print(pens)

for angle in range(100):
    for p in pens:   
        p.forward(10)
        p.left(angle)

turtle.mainloop()
