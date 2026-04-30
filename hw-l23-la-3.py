import turtle
turtle.setup(600,400)
t = turtle.Turtle()
t.hideturtle()
colors = ["lime", "blue", "orange", "teal"]
clicks = 0
def clicked(x,y):
  global clicks
  t.pencolor(colors[clicks])
  t.pensize(150)
  t.fd(0)
  clicks += 1
  if clicks == 4:
    clicks = 0
turtle.onscreenclick(clicked)
turtle.mainloop()
