import turtle,random

turtle.setup(600,400)

t=turtle.Turtle()

t.speed(2)
def get_randomnumber(x,y):
  n = random.randint(1,100)
  print("Random number:",n)

def say_hello(x,y):
  print("Hello!", x, y)
def draw_box(x,y):
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.color(random.choice(["red", "blue", "green", "yellow", "orange", "purple"]))
  t.begin_fill()
  for i in range(4):
    t.forward (random.randint(50,100))
    t.left(90)
  
  t.end_fill()
  t.penup()


turtle.onscreenclick(say_hello,1)
turtle.onscreenclick(get_randomnumber,3)
turtle.onscreenclick(draw_box,1)

turtle.mainloop()

