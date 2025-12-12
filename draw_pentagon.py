import turtle

# Create a turtle object
t = turtle.Turtle()
t.speed(2)

# Draw a square
print("Drawing a square...")
t.color("blue")
for i in range(4):
    t.forward(100)
    t.right(90)

# Move to a new position
t.penup()
t.goto(-150, 0)
t.pendown()

# Draw a pentagon
print("Drawing a pentagon...")
t.color("red")
for n in range(10):
    t.forward(100)
    t.right(40)

# Keep the window open
turtle.done()
