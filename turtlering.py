import turtle
width = int(input("Put width: "))
height = int(input("Put height: "))
turtle.setup(width, height)
if width >= height:
  numberr = width
else:
  numberr = height
t = turtle.Turtle()
t.penup()
t.setpos(0 - (numberr / 2), numberr / 2)
t.speed(1000)
t.pendown()
for i in range(numberr * 2):
  t.forward(numberr - i)
  t.right(90)
turtle.done()
