import sys, os
_NIX_PY = "/nix/store/pjn7rx1d3jnjsif6wnz5im0fdm8pp7xa-python3-3.11.13/bin/python3"
if os.path.exists(_NIX_PY) and os.environ.get("TKINTER_READY") != "1":
    os.environ["TKINTER_READY"] = "1"
    os.execv(_NIX_PY, [_NIX_PY] + sys.argv)

import turtle
import random
print("Question 1\n")
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
print("\nQuestion 2\n")
