import turtle

wn = turtle.Screen()
wn.title("Mouse Click Counter")

click_count = 0

def handle_click(x, y):
    global click_count
    click_count += 1
    print(click_count)

wn.onscreenclick(handle_click, 1)
wn.listen()
wn.mainloop()
