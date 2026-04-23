import turtle


def count(x, y):
    global counter
    counter += 1
    p.clear()
    p.write("Counter: " + str(counter), font=("Calibri", 15, "normal"))


turtle.setup(600, 400)
p = turtle.Pen()

counter = 0
p.clear()
p.write("Counter: " + str(counter), font=("Calibri", 15, "normal"))

turtle.onscreenclick(count, 1)


turtle.mainloop()
