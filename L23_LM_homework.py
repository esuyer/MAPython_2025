import turtle

screen = turtle.Screen()
screen.title("Left and Right Click Counters")
screen.bgcolor("white")

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

left_count = 0
right_count = 0

def update_display():
    writer.clear()
    writer.goto(0, 50)
    writer.write("Left clicks: " + str(left_count), align="center", font=("Arial", 20, "bold"))
    writer.goto(0, 0)
    writer.write("Right clicks: " + str(right_count), align="center", font=("Arial", 20, "bold"))

def left_click(x, y):
    global left_count
    left_count += 1
    update_display()

def right_click(x, y):
    global right_count
    right_count += 1
    update_display()

update_display()

screen.onclick(left_click, btn=1)
screen.onclick(right_click, btn=3)
screen.mainloop()
