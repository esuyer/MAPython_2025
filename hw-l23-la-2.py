import turtle
turtle.setup(600,400)
t = turtle.Turtle()
clicks = 0
def clicked(x,y):
  global clicks
  clicks += 1
  t.clear()
  t.write(f"clicked {clicks} times")
turtle.onscreenclick(clicked)
turtle.mainloop()
