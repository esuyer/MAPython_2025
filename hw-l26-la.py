from ctypes.wintypes import HRGN
import turtle
import time
from datetime import datetime
turtle.setup(600,400)
turtle.mode("logo")
#                  --Visuals--
visual = turtle.Turtle()
visual.speed(0)
visual.up()
visual.lt(90)
visual.bk(100)
visual.rt(90)
visual.pendown()
for i in range(60):
  if i % 5 == 0:
    visual.lt(90)
    visual.fd(25)
    visual.bk(25)
    visual.rt(90)
  else:
    visual.lt(90)
    visual.fd(10)
    visual.bk(10)
    visual.rt(90)
  visual.begin_poly()
  visual.circle(100,6)
  visual.end_poly()
visual.penup()
visual.lt(90)
visual.fd(100)
visual.shape("circle")
#               --Hands & Digital--

sec = turtle.Turtle()
sec.speed(0)
sec.pendown()
min = turtle.Turtle()
min.speed(0)
min.pendown()
hr = turtle.Turtle()
hr.speed(0)
hr.pendown()

#digital = 

sec.pensize(1)
sec.color("black")
sec.seth(datetime.now().time().second * 6)
sec.fd(80)
sec.bk(80)

min.pensize(2)
min.color("black")
min.seth(datetime.now().minute * 6)
min.fd(60)
min.bk(60)

hr.pensize(3)
hr.color("black")
hr.seth((datetime.now().hour - 4) * 30)
hr.fd(40)
hr.bk(40)
while True:
  now = datetime.now()
  #                      --Hands--
  # --Hour--
  if now.time().hour - 4 < datetime.now().time().hour - 4:
    # --Clearing--
    hr.clear()

    # --Drawing--

    hr.pensize(3)
    hr.color("black")
    hr.seth((now.time().hour - 4) * 30)
    hr.fd(40)
    hr.bk(40)
  # --Minute--
  if now.time().minute < datetime.now().time().minute:
    # --Clearing--
    min.clear()

    # --Drawing--

    min.pensize(2)
    min.color("black")
    min.seth(now.time().minute * 6)
    min.fd(60)
    min.bk(60)
  # --Second--
  if now.time().second < datetime.now().time().second:
    # --Clearing--
    sec.clear()
    
    print(now)
    
    # --Drawing--
    sec.pensize(1)
    sec.color("black")
    sec.seth(now.time().second * 6)
    sec.fd(80)
    sec.bk(80)

  #                   --Digital--
  #now = datetime.now()
  #now.hour -= 4
  #formatted_time = now.strftime("%H:%M:%S")
  
  
  
