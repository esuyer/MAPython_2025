import turtle

x_speed = 3
y_speed = 3

# Paddle
paddle = turtle.Pen()
paddle.shape("square")
paddle.shapesize(0.5, 6)
paddle.color("blue")
paddle.speed(0)
paddle.up()
paddle.goto(0, -160)


def left():
    paddle.setheading(180)
    paddle.forward(10)


def right():
    paddle.setheading(0)
    paddle.forward(10)


turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.listen()

# Ball
ball = turtle.Pen()
ball.shape("circle")
ball.color("red")
ball.speed(0)
ball.up()
ball.goto(-100, 100)


# Game Tick
def tick():
    global x_speed
    global y_speed
    x = ball.xcor() + x_speed
    y = ball.ycor() + y_speed
    ball.goto(x, y)

    # Bounce off Ceiling
    if y > 200:
        y_speed = -1 * y_speed

    # Bounce off WallR
    if x > 300:
        x_speed = -1 * x_speed

    # Bounce off WallL
    if x < -300:
        x_speed = -1 * x_speed

    # Bounce of paddle
    if ball.distance(paddle) < 50 and y < -160 and y_speed < 0:
        y_speed = -1 * y_speed

    turtle.update()
    turtle.ontimer(tick, 17)


turtle.setup(600, 400)
turtle.tracer(0)
tick()


turtle.mainloop()
