import turtle, random

turtle.setup(600, 400)

# Create a turtle object
#t = turtle.Turtle()
#t.speed(2)

# randon number generator callback function
def get_randomnumber(x, y):
  n = random.randint(1,100)
  print("Random number:", n)

# Create a callback function
def say_hello(x, y):
    print("Hello!", x, y)

turtle.onscreenclick(get_randomnumber, 3)



"""
Problem 1. Click and draw
Write a program that draws a square at the location of the left mouse click. Choose the color of the
square randomly.

Make the squares filled with color. The code below shows how to do it:
pen = turtle.Pen()
pen.begin_fill()

#draw the shape here
pen.end_fill()

Make the size of the squares random too. You can also change the background color using the
function turtle.bgcolor.
"""
print ("Problem 1")
def draw_square(x, y):
    t = turtle.Turtle()
    t.speed(2)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(random.choice(["red", "blue", "green", "yellow", "orange", "purple"]))
    t.begin_fill()
    for i in range(4):
        t.forward(random.randint(10, 100))
        t.right(90)

    t.end_fill()
    t.hideturtle()

turtle.onscreenclick(draw_square, 1)


"""
Problem 2. Connect with corners
Write a program that draws lines from the 4 corners of the canvas to the location of the left mouse
click. Choose the color of the lines randomly.

Tip: to determine the coordinates of the corners of the canvas look at the numbers given to
turtle.setup function. For example, if the canvas is set up using turtle.setup(600, 400), then
its width is 600 pixels, and its height is 400 pixels.
Reminder: the center of the coordinates (0, 0) is in the in the center of the canvas.
"""

"""
Problem 3. Flowers on click
1). Write a program that draws a flower when the left mouse button is clicked. The center of the flower
should be at the location of the click.

This flower has 10 “petals”. Each petal is a line that has a length of 20.

The header of the function could look like this:
def draw_flower(x, y):
Tip: function backward will be useful for returning the pen back to the center of the flower.

2). Make your program choose a random color for the pen when the right mouse button is clicked.
(You will need to write a separate function for handling right mouse clicks.)

Spray paint (Challenge)
Write a program that responds to a left click by stamping
10 small circles “in the vicinity” of the location of the click.
“In the vicinity” means in range (-10, 10) in both directions
from the coordinate of the click.

On right click set a random color to the pen.

(x, y)

(x, y) – location of the
click
(x + 10, y +
10)

(x - 10, y -
10)

Four turtles (Challenge)
Create 4 pens of different colors: green, red, blue, and purple. They all should start at (0, 0).
Handle the left mouse clicks as follows:
- Relocates the green pen to the location of the left
mouse click (it should draw a line as it moves
around)
- Relocates 3 other pens so that they mirror the
motions of the green one with respect to the x-axis,
y-axis, and with respect to the center of coordinates.
(See picture on the right for an example of a single
move)

"""

# Create a mouse click event
turtle.mainloop()
