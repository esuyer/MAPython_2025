import turtle

screen = turtle.Screen()
screen.title("Click Counter")
screen.bgcolor("white")

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

counter = 0

def count_click(x, y):
    global counter
    counter += 1
    writer.clear()
    writer.goto(0, 0)
    writer.write(counter, align="center", font=("Arial", 30, "bold"))

screen.onclick(count_click)
screen.mainloop()
