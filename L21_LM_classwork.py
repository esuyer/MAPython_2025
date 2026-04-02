import turtle
import random

screen = turtle.Screen()
screen.title("Click to Draw Squares")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

colors = ["red", "blue", "green", "orange", "purple", "pink", "yellow", "cyan", "magenta", "coral"]

def draw_square(x, y):
    color = random.choice(colors)
    size = random.randint(20, 100)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

screen.onclick(draw_square)
screen.mainloop()
