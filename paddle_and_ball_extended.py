import turtle
import random


def left():
    paddle.setheading(180)
    if paddle.xcor() > -240:
        paddle.forward(10)


def right():
    paddle.setheading(0)
    if paddle.xcor() < 240:
        paddle.forward(10)


def new_game():
    global x_speed
    global y_speed
    global lost
    global caught
    x_speed = 5
    y_speed = 5
    lost = 0
    caught = 0


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
            caught = caught + 1

    if y < -200:
        lost += 1
        ball.goto(random.randint(-200, 200), 160)

    info = "Lost: " + str(lost) + " Caught: " + str(caught)
    if lost == 5:
        x_speed = 0
        y_speed = 0
        info = info + " GAME OVER! Press N to start a new game."

    pen.clear()
    pen.write(info, font=("Consolas", 12, "normal"))

    turtle.update()

    screen.ontimer(tick, 17)


turtle.setup(600, 400)
turtle.tracer(0)

screen = turtle.Screen()

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
pen.goto(-280, 160)

screen.onkeypress(left, "s")
screen.onkeypress(right, "d")
screen.onkey(new_game, "n")

tick()

screen.listen()

turtle.mainloop()
