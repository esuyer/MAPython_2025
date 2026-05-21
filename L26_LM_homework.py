import turtle
import random

print("Question 1\n")
screen = turtle.Screen()
screen.setup(width=600, height=600)
'''
pen = turtle.Turtle()
pen.speed(0)

def draw_random():
    r = random.random()
    g = random.random()
    b = random.random()
    pen.pencolor(r, g, b)

    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    pen.goto(x, y)

    screen.ontimer(draw_random, 100)

pen.pendown()
draw_random()

turtle.mainloop()
'''
print("\nQuestion 2\n")
'''
pen2 = turtle.Turtle()
pen2.speed(0)

def draw_pentagon():
    r = random.random()
    g = random.random()
    b = random.random()
    pen2.pencolor(r, g, b)
    pen2.fillcolor(r, g, b)

    x = random.randint(-270, 270)
    y = random.randint(-270, 270)
    pen2.penup()
    pen2.goto(x, y)
    pen2.pendown()

    pen2.begin_fill()
    for _ in range(5):
        pen2.forward(60)
        pen2.left(72)
    pen2.end_fill()

    screen.ontimer(draw_pentagon, 500)

draw_pentagon()

turtle.mainloop()
'''
print("\nQuestion 3\n")
def sum_word_lengths(words):
    total = 0
    for word in words:
        total += len(word)
    return total

word_list = ["apple", "banana", "cherry", "blueberry", "strawberry"]
print(sum_word_lengths(word_list))

print("\nQuestion 4\n")
def secret_message(words):
    message = ""
    for i, word in enumerate(words):
        if i < len(word):
            message += word[i]
    return message
word_list = ["apple", "banana", "cherry", "blueberry", "strawberry"]
print(secret_message(word_list))

print("\nQuestion 5\n")
pen3 = turtle.Pen()
pen3.color("blue")
pen3.speed(0)

word = "Python"
letter_index = 0
color_index = 0

for i in range(36):
    if letter_index == 0:
        r = random.random()
        g = random.random()
        b = random.random()
        pen3.color(r, g, b)

    pen3.forward(15)
    pen3.write(word[letter_index])
    pen3.right(10)

    letter_index += 1
    if letter_index >= len(word):
        letter_index = 0

turtle.mainloop()