import turtle
import random
turtle.setup(800, 600)
pen = turtle.Pen()
pen.shape("turtle")
pen.hideturtle() 
pen.up()
N = random.randint(5, 10)

for i in range(N):
  if i%2==1:
    pen.color("red")
  if i%2==0:
    pen.color("green")
  pen.stamp()
  pen.forward(50)
  
turtle.done()


