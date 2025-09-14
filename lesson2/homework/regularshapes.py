import turtle

pen = turtle.Pen()
pen.width(3)
pen.color("orange")

for i in range(6):
    pen.forward(100)
    pen.left(60)

pen.up()
pen.goto(-200, -200)
pen.color("red")
pen.down()

for i in range(5):
    pen.forward(200)
    pen.right(144)
    
turtle.mainloop()
