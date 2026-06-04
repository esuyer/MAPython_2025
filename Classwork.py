import turtle
import random
import time
screen = turtle.Screen()
color = ["red", "green", "blue", "yellow", "purple", "orange"]
def draw_circle_with_stamp():
   time.sleep(500)
   t = turtle.Turtle()
   t.shape("circle")
   t.color(random.choice(color))
   t.stamp()
   t.penup()
   t.goto(random.randint(-200, 200), random.randint(-200, 200))
   t.pendown()
   t.circle(random.randint(10, 50))
for i in range(random.randint(10,100)):
 draw_circle_with_stamp()
screen.mainloop()