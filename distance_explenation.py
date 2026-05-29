import sys, os
_NIX_PY = "/nix/store/pjn7rx1d3jnjsif6wnz5im0fdm8pp7xa-python3-3.11.13/bin/python3"
if os.path.exists(_NIX_PY) and os.environ.get("TKINTER_READY") != "1":
    os.environ["TKINTER_READY"] = "1"
    os.execv(_NIX_PY, [_NIX_PY] + sys.argv
            )


import turtle


rectangle = turtle.Pen()
rectangle.shape("square")
rectangle.color("green")
rectangle.shapesize(1, 8)

circle = turtle.Pen()
circle.color("red")
circle.shape("circle")
##circle.goto(-50, 0)
circle.goto(0, 50)

print(rectangle.distance(circle))

turtle.mainloop()
