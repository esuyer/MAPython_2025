import turtle
import random

screen = turtle.Screen()
screen.title("Keyboard Drawing")
screen.bgcolor("white")

mike = turtle.Turtle()
mike.speed(0)
mike.width(1)

def move_left():
    mike.setheading(180)
    mike.forward(5)

def move_right():
    mike.setheading(0)
    mike.forward(5)

def move_up():
    mike.setheading(90)
    mike.forward(5)

def move_down():
    mike.setheading(270)
    mike.forward(5)

def set_red():
    mike.pencolor("red")

def set_green():
    mike.pencolor("green")

def set_blue():
    mike.pencolor("blue")

# Step 3 - Random color

def set_random_color():
    colors = ["red", "blue", "green", "orange", "purple", "pink", "yellow", "cyan", "magenta", "coral"]
    mike.pencolor(random.choice(colors))

# Step 4a - Increase pen width

def increase_width():
    current = mike.width()
    if current < 20:
        mike.width(current + 1)

def decrease_width():
    current = mike.width()
    if current > 1:
        mike.width(current - 1)

# Bind keys
screen.listen()

screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")

screen.onkeypress(set_red, "r")
screen.onkeypress(set_green, "g")
screen.onkeypress(set_blue, "b")

screen.onkeypress(set_random_color, "c")

screen.onkeypress(increase_width, "z")
screen.onkeypress(decrease_width, "x")

screen.mainloop()
