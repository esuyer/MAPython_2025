import turtle
import random


def left():
    paddle.setheading(180)
    paddle.forward(10)


def right():
    paddle.setheading(0)
    paddle.forward(10)


def tick():
    global x_speed
    global y_speed
    global lost
    global caught

    x = ball.xcor()
    y = ball.ycor()
    x += x_speed
    y += y_speed
    ball.goto(x, y)

    if x > 280 or x < -280:
        ball.color(random.random(), random.random(), random.random())
        x_speed = -x_speed

    if y > 180:
        ball.color(random.random(), random.random(), random.random())
        y_speed = -y_speed

    if y > -160 and y < -140:
        if ball.distance(paddle) < 50 and y_speed < 0:
            y_speed = -y_speed
            caught += 1
            pen.clear()
            pen.write(
                "Caught: " + str(caught) + "  Missed: " + str(lost),
                font=("Consolas", 15, "normal"),
            )

    if y < -200:
        lost += 1
        pen.clear()
        pen.write(
            "Caught: " + str(caught) + "  Missed: " + str(lost),
            font=("Consolas", 15, "normal"),
        )
        ball.goto(random.randint(-200, 200), 160)

    turtle.update()

    turtle.ontimer(tick, 17)


turtle.setup(600, 400)
turtle.tracer(0)


ball = turtle.Pen()
ball.shape("circle")
ball.color(random.random(), random.random(), random.random())
ball.speed(0)
ball.up()
ball.goto(-200, 100)
x_speed = 5
y_speed = 5

lost = 0
caught = 0

paddle = turtle.Pen()
paddle.shape("square")
paddle.shapesize(0.5, 6)
paddle.color("green")
paddle.speed(0)
paddle.up()
paddle.goto(0, -160)

pen = turtle.Pen()
pen.up()
pen.goto(-250, 160)
pen.write(
    "Caught: " + str(caught) + "  Missed: " + str(lost), font=("Consolas", 15, "normal")
)

turtle.onkeypress(left, "s")
turtle.onkeypress(right, "d")

tick()

turtle.listen()

turtle.mainloop()
