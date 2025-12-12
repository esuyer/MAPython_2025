import turtle

#username = input ("what is your name?")
#print("hello", username)

#food = input("what is your favorite food?")
#print(username, "likes", food)

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

# Draw a stair case
t.forward(40)
t.left(90)
t.forward(40)
t.right(90)
t.forward(40)



# Keep the window open
turtle.done()