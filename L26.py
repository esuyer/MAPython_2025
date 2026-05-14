import time
import turtle

start = time.time()

'''
def kaboom():
  pen.write("KABOOM!", font=("Arial", 20, "normal"))

pen = turtle.Pen()
turtle.ontimer(kaboom, 5000)

'''

turtle.clearscreen()
turtle.setup(600, 400)

mike  = turtle.Pen()
mike.shape("turtle")
mike.speed(0)
mike.up()
mike.goto(-200, 0)

def move():
  x = mike.xcor()
  turtle.write( + " ")
  mike.forward(5)

  if x > 200:
    mike.left(180)
    mike.forward(5)

  turtle.ontimer(move, 100)

move()

turtle.mainloop()

end = time.time()
print(end - start)
