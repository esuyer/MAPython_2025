import sys, os
_NIX_PY = "/nix/store/pjn7rx1d3jnjsif6wnz5im0fdm8pp7xa-python3-3.11.13/bin/python3"
if os.path.exists(_NIX_PY) and os.environ.get("TKINTER_READY") != "1":
    os.environ["TKINTER_READY"] = "1"
    os.execv(_NIX_PY, [_NIX_PY] + sys.argv)

import turtle

def squares(size, depth):
    global counter

    # exit condition
    if depth == 0:
        return

    # alternate colors
    if counter % 2 == 0:
        p.color("green")
    else:
        p.color("yellow")

    counter += 1

    # draw the square
    p.begin_fill()
    for i in range(4):
        p.forward(size)
        p.left(90)
    p.end_fill()

    # move to the next square
    p.forward(size)

    # recursive call
    squares(size * 3 / 4, depth - 1)
    



p = turtle.Pen()
p.up()
p.goto(-250, 0)
p.down()

# initialize counter
counter = 0

squares(100, 7)

turtle.mainloop()

