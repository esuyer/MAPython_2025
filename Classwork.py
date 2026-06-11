import turtle

screen = turtle.Screen()
screen.setup(1000, 1000)

pen = turtle.Turtle()
pen.speed(0)

def square(size, color):
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(4):
        pen.forward(size)
        pen.left(90)
    pen.end_fill()

def line_squares(size, level, color="green"):
    if level == 0:
        return

    square(size, color)

    next_color = "yellow"
    if color == "yellow":
        next_color = "green"

    pen.forward(size)
    line_squares(size / 2, level - 1, next_color)
    pen.backward(size)

def hexagon(size):
    for i in range(6):
        pen.forward(size)
        pen.left(60)

def hexagon_fractal(size, level):
    if level == 0:
        return
    hexagon(size)
    for i in range(6):
        pen.forward(size)
        hexagon_fractal(size / 3, level - 1)
        pen.backward(size)
        pen.left(60)

def triangle(size):
    for i in range(3):
        pen.forward(size)
        pen.left(120)

def sierpinski(size, level):
    if level == 0:
        triangle(size)
        return

    sierpinski(size / 2, level - 1)

    pen.forward(size / 2)
    sierpinski(size / 2, level - 1)
    pen.backward(size / 2)

    pen.left(60)
    pen.forward(size / 2)
    pen.right(60)

    sierpinski(size / 2, level - 1)

    pen.left(60)
    pen.backward(size / 2)
    pen.right(60)

def snowflake(length, level):
    if level == 0:
        pen.forward(length)
        pen.backward(length)
        return

    for i in range(6):
        pen.forward(length)
        snowflake(length / 3, level - 1)
        pen.backward(length)
        pen.left(60)

def two_corners(size, level):
    if level == 0:
        square(size, "white")
        return

    square(size, "white")

    two_corners(size / 2, level - 1)

    pen.penup()
    pen.forward(size)
    pen.left(90)
    pen.forward(size)
    pen.right(90)
    pen.pendown()

    two_corners(size / 2, level - 1)

    pen.penup()
    pen.backward(size)
    pen.right(90)
    pen.backward(size)
    pen.left(90)
    pen.pendown()

pen.penup()
pen.goto(-400, 250)
pen.pendown()
line_squares(100, 5)

pen.color("black")
pen.penup()
pen.goto(100, 250)
pen.pendown()
hexagon_fractal(90, 3)

pen.penup()
pen.goto(-350, -50)
pen.pendown()
sierpinski(200, 4)

pen.penup()
pen.goto(200, -50)
pen.pendown()
snowflake(60, 3)

pen.penup()
pen.goto(-100, -300)
pen.pendown()
two_corners(120, 4)

turtle.done()