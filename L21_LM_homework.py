import turtle
import random

screen = turtle.Screen()
screen.title("Click to Draw Triangles")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

colors = ["red", "blue", "green", "orange", "purple", "pink", "yellow", "cyan", "magenta", "coral"]

def draw_triangle(x, y):
    color = random.choice(colors)
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(80)
        t.left(120)
    t.end_fill()

screen.onclick(draw_triangle)
screen.mainloop()
