import sys, os
_NIX_PY = "/nix/store/pjn7rx1d3jnjsif6wnz5im0fdm8pp7xa-python3-3.11.13/bin/python3"
if os.path.exists(_NIX_PY) and os.environ.get("TKINTER_READY") != "1":
    os.environ["TKINTER_READY"] = "1"
    os.execv(_NIX_PY, [_NIX_PY] + sys.argv)


import turtle, random

turtle.setup(600, 400)
turtle.clearscreen()


def say_score():
  t.pendown()
  score = 125
  t.write("Score: " + str(score), font=("Arial", 16, "normal"))

def move_left():
  t.pendown()
  t.setheading(180)
  t.forward(100)
  

turtle.onkeypress(say_score, "a")
turtle.onkeypress(move_left, "Left")

turtle.listen()
turtle.mainloop()