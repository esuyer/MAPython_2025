import turtle

screen = turtle.Screen()
screen.title("Color Cycle Circle")
screen.bgcolor("white")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
index = 0

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(0, -50)
t.pendown()
t.fillcolor(colors[index])
t.begin_fill()
t.circle(50)
t.end_fill()

def change_color(x, y):
    global index
    index = (index + 1) % len(colors)
    t.clear()
    t.fillcolor(colors[index])
    t.begin_fill()
    t.circle(50)
    t.end_fill()

screen.onclick(change_color)
screen.mainloop()
