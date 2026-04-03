import turtle
import random

screen = turtle.Screen()
screen.title("Right Click to Draw Lines from Corners")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

colors = ["red", "blue", "green", "orange", "purple", "pink", "yellow", "cyan", "magenta", "coral"]

width = screen.window_width() // 2
height = screen.window_height() // 2

corners = [(-width, height), (width, height), (width, -height), (-width, -height)]

def draw_lines(x, y):
    for corner in corners:
        color = random.choice(colors)
        t.penup()
        t.goto(corner)
        t.pencolor(color)
        t.pendown()
        t.goto(x, y)

screen.onclick(draw_lines, btn=3)
screen.mainloop()
