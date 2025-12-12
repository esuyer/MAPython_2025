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
t.goto(150, 0)
t.pendown()

# Draw a triangle
print("Drawing a triangle...")
t.color("red")
for i in range(3):
    t.forward(100)
    t.right(120)

# Move to a new position
t.penup()
t.goto(-150, 0)
t.pendown()

# Draw a circle
print("Drawing a circle...")
t.color("green")
t.circle(50)

# Keep the window open
turtle.done()
