import sys, os
_NIX_PY = "/nix/store/pjn7rx1d3jnjsif6wnz5im0fdm8pp7xa-python3-3.11.13/bin/python3"
if os.path.exists(_NIX_PY) and os.environ.get("TKINTER_READY") != "1":
    os.environ["TKINTER_READY"] = "1"
    os.execv(_NIX_PY, [_NIX_PY] + sys.argv
            )
import turtle

y_speed = 3
x_speed = 3
caught = 0
lost = 0

# One game tick
def tick():
  global y_speed
  global x_speed
  global caught
  global lost
  
  x = ball.xcor() + x_speed
  y = ball.ycor() + y_speed
  ball.goto(x, y)

  # bouncing off the top / ceiling
  if y > 200:
    y_speed = -1 * y_speed

  # bouncing off the right wall
  if x > 300:
    x_speed = -1 * x_speed
    
  # bouncing off the left wall
  if x < -300:
    x_speed = -1 * x_speed

  # bouncing off the bottom / floor
  if y < -200:
    y_speed = -1 * y_speed

  # bouncing off the paddle
  if ball.distance(paddle) < 50 and y < -160 and y_speed < 0:
    y_speed = -1 * y_speed
    caught += 1
    pen.clear()
    pen.write(
        "Caught: " + str(caught) + "  Missed: " + str(lost),
        font=("Consolas", 15, "normal"),
    )

  # missing the ball with the paddle
  if y < -200:
    lost += 1
    pen.clear()
    pen.write(
        "Caught: " + str(caught) + "  Missed: " + str(lost),
        font=("Consolas", 15, "normal"),
    )

     
  
    


  turtle.update()            # update the canvas

  turtle.ontimer(tick, 17)   # scheduling the next tick in 17 ms


turtle.setup(600, 400)
turtle.tracer(0)             # 0 means do not update the canvas until function turtle.update() is called

# Game objects: paddle and ball 
paddle = turtle.Pen()
paddle.shape("square")
paddle.shapesize(0.5, 6)
paddle.color("green")
paddle.speed(0)
paddle.up()
paddle.goto(0, -160)

ball = turtle.Pen()
ball.shape("circle")
ball.color("red")
ball.speed(0)
ball.up()
ball.goto(-100, 100)

def left():
  paddle.setheading(180)
  paddle.forward(10)

def right():
  paddle.setheading(0)
  paddle.forward(10)

pen = turtle.Pen()
pen.up()
pen.goto(-250, 160)
pen.write(
    "Caught: " + str(caught) + "  Missed: " + str(lost), font=("Consolas", 15, "normal")
)

turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")

turtle.listen()




# Starting the game loop (the first tick)

tick()

turtle.mainloop()