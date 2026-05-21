import time
import turtle
import random
start = time.time()


mike=turtle.Turtle()
mike.shape("turtle")
mike.speed(0)
mike.up()

def line():
  turtle.ontimer(line,100)
  mike.down()
  mike.goto(random.randint(-300,300),random.randint(-200,200))
  mike.color(random.choice(["red", "blue", "green", "yellow", "orange", "purple"]))
line()

turtle.mainloop()
end=time.time()