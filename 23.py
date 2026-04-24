

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
