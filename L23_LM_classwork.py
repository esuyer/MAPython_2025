import turtle

screen = turtle.Screen()
screen.title("Click Counter")
screen.bgcolor("white")

counter = 0

def count_click(x, y):
    global counter
    counter += 1
    print(counter)

screen.onclick(count_click)
screen.mainloop()
