import random
import turtle
import time
print("Question 1\n")

screen = turtle.Screen()
screen.title("Random circles")

def draw_line_and_stamp(x, y):
  r = random.random()
  g = random.random()
  b = random.random()
  pen.color(r, g, b)

  pen.penup()
  pen.goto(x, y)
  pen.stamp()

pen = turtle.Turtle()
pen.speed(0) 
pen.shape("circle")
pen.shapesize(1) 

screen.onclick(draw_line_and_stamp)
turtle.mainloop()
