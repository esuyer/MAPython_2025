import turtle
import random

screen = turtle.Screen()

mode = 1

left_count = 0
right_count = 0

left_pen = turtle.Turtle()
left_pen.hideturtle()
left_pen.penup()
left_pen.goto(-200, 200)

right_pen = turtle.Turtle()
right_pen.hideturtle()
right_pen.penup()
right_pen.goto(100, 200)

flower_pen = turtle.Turtle()
flower_pen.speed(0)

def handle_click(x, y):
    global left_count, right_count

    if mode == 1:
        left_count += 1
        left_pen.clear()
        left_pen.write("Left: " + str(left_count), font=("Arial", 14, "normal"))

    elif mode == 2:
        flower_pen.penup()
        flower_pen.goto(0, 0)
        flower_pen.pendown()
        flower_pen.pencolor(random.random(), random.random(), random.random())
        flower_pen.goto(x, y)
        flower_pen.penup()
        flower_pen.stamp()

def handle_right(x, y):
    global right_count
    if mode == 1:
        right_count += 1
        right_pen.clear()
        right_pen.write("Right: " + str(right_count), font=("Arial", 14, "normal"))

def switch_mode():
    global mode
    mode += 1
    if mode > 2:
        mode = 1
    left_pen.clear()
    right_pen.clear()
    flower_pen.clear()

screen.listen()
screen.onkey(switch_mode, "space")

screen.onclick(handle_click, btn=1)
screen.onclick(handle_right, btn=3)

def unimportant_pos(W, N):
    return W[:N] + W[N+1:]

def sue_word(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return "Favorite"
    return "Boring"

def same_weight(lst):
    if len(lst) == 0:
        return "Pass"
    first = lst[0]
    for w in lst:
        if w != first:
            return "Fail"
    return "Pass"

turtle.done()