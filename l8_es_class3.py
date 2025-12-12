import turtle

# Create a turtle object
t = turtle.Turtle()
t.speed(2)

# Draw a square
def draw_square(size, color):
    t.color(color)
    t.pensize(5)
    for i in range(4):
        t.forward(size)
        t.right(90)

draw_square(100, "blue")
draw_square(50, "red")

# Keep the window open
turtle.done()
