import turtle

def draw_grid(N, L):
    t = turtle.Turtle()
    t.speed(0)
    for i in range(N + 1):
        t.penup()
        t.goto(0, i * L)
        t.pendown()
        t.forward(N * L)
    t.left(90)
    for i in range(N + 1):
        t.penup()
        t.goto(i * L, 0)
        t.pendown()
        t.forward(N * L)
    turtle.done()

draw_grid(5, 100)
