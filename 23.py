import sys, os

_NIX_PY = "/nix/store/pjn7rx1d3jnjsif6wnz5im0fdm8pp7xa-python3-3.11.13/bin/python3"
if os.path.exists(_NIX_PY) and os.environ.get("TKINTER_READY") != "1":
    os.environ["TKINTER_READY"] = "1"
    os.execv(_NIX_PY, [_NIX_PY] + sys.argv)

import turtle

wn = turtle.Screen()
wn.title("Mouse Click Counter")

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

click_count = 0


def handle_click(x, y):
    global click_count
    click_count += 1
    writer.clear()
    writer.write(click_count, align="center", font=("Arial", 24, "normal"))


wn.onscreenclick(handle_click, 1)
wn.listen()
wn.mainloop()
