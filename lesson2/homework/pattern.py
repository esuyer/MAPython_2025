import turtle

p = turtle.Pen()
p.width(2)
p.speed(0)

p.up()
p.goto(-250, 0)
p.down()

for i in range(10):
    p.color("magenta")
    p.forward(30)
    p.left(90)
    p.color("red")
    p.forward(30)
    p.right(90)
    p.color("green")
    p.forward(30)
    p.right(90)
    p.color("blue")
    p.forward(30)
    p.left(90)

    
turtle.mainloop()

    



    
