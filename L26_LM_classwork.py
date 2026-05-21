import random
import turtle

print("Question 1\n")
'''
screen = turtle.Screen()
screen.title("Random circles")

pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.shapesize(1)

def draw_dot():
    r = random.random()
    g = random.random()
    b = random.random()
    pen.color(r, g, b)
    pen.penup()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    pen.goto(x, y)
    pen.stamp()
    screen.ontimer(draw_dot, 500)

def draw_line_and_stamp(x, y):
    r = random.random()
    g = random.random()
    b = random.random()
    pen.color(r, g, b)
    pen.penup()
    pen.goto(x, y)
    pen.stamp()

screen.onclick(draw_line_and_stamp)
draw_dot()
turtle.mainloop()
'''
print("\nQuestion 2\n")
drop = turtle.Pen()
drop.shape("circle")
drop.shapesize(2)
drop.speed(0)

turtle.mainloop()
