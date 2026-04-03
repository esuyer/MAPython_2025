import turtle
import random

screen = turtle.Screen()
screen.title("Click to Draw Squares")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

colors = ["red", "blue", "green", "orange", "purple", "pink", "black", "cyan", "magenta", "coral"]

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

print("Question 2\n")
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