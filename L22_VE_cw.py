import turtle, random

turtle.setup(600,400)
turtle.clearscreen()
screen= turtle.Screen()
t=turtle.Turtle()
t.speed(2)

def say_score():
  t=turtle.Turtle()
  t.speed(2)
  t.pendown()
  score=125
  t.write("score: " + str(score), font=("Arial", 16, "normal"))


def move_left():
  t.setheading(180)
  t.forward(100)

def move_right():
  t.setheading(0)
  t.forward(100)

def move_up():
  t.setheading(90)
  t.forward(100)

def move_down():
  t.setheading(270)
  t.forward(100)

def pen_width():
  curent_width=t.width()
  if curent_width<20:
    t.width(curent_width + 1)

def decrease_width():
  curent_width=t.width()
  if curent_width>1:
    t.width(curent_width - 1)


def increase_width():
  


  
  


screen.onkeypress(say_score, "a")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_down, "Down")
screen.onkeypress(pen_width, "z")
screen.onkeypress(move_up, "Up")
screen.onkeypress(decrease_width, "x")

screen.listen()
screen.mainloop()