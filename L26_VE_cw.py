import sys, os
_NIX_PY = "/nix/store/pjn7rx1d3jnjsif6wnz5im0fdm8pp7xa-python3-3.11.13/bin/python3"
if os.path.exists(_NIX_PY) and os.environ.get("TKINTER_READY") != "1":
    os.environ["TKINTER_READY"] = "1"
    os.execv(_NIX_PY, [_NIX_PY] + sys.argv)


import time
import turtle
import random
start = time.time()




#def kaboom():
#  pen.write("KABOOM!", font=("Arial", 20, "normal"))

#pen=turtle.Pen()
#turtle.ontimer(kaboom,5000)


turtle.setup(600,400)

mike=turtle.Turtle()
mike.shape("turtle")
mike.speed(0)
mike.up()

def circle():
  turtle.ontimer(circle,500)
  mike.up()
  mike.goto(random.randint(-300,300),random.randint(-200,200))
  mike.down()
  mike.color(random.choice(["red", "blue", "green", "yellow", "orange", "purple"]))
  mike.begin_fill()
  mike.circle(20)
  mike.end_fill()
circle()

'''
def move():
  x=mike.xcor()
  mike.forward(5)
  turtle.ontimer(move,10)
  if x>200:
    mike.left(100)
    mike.forward(5)
'''

turtle.mainloop()

end=time.time()
duration=end-start