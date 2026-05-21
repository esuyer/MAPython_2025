import turtle
import random
screen = turtle.Screen()
screen.setup(width=600, height=600)
pen = turtle.Turtle()
pen.speed(0)
def doodle():
    r = random.random()
    g = random.random()
    b = random.random()
    pen.pencolor(r, g, b)
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    pen.goto(x, y)
    screen.ontimer(doodle, 100)
doodle()
turtle.done()

    