import src.turtle_shim
import turtle
import random

def run_classwork():
    screen = turtle.Screen()
    screen.title("Classwork (Turtle Shim)")
    
    t = turtle.Turtle()
    t.speed(0)
    t.color("cyan")
    
    # Draw pattern
    for _ in range(36):
        for _ in range(4):
            t.forward(100)
            t.right(90)
        t.right(10)
    
    turtle.done()

if __name__ == "__main__":
    run_classwork()

sp = 4
pens=[]
for i in range(sp):
  p = turtle.Pen()
  p.pencolor("green")
  p.pensize(2)
  pens.append(p)
for i in range(pens):
  p.forward(100)
  
  