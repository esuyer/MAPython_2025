import random
import turtle
print("Question 1: \n")
count = 0
for i in range(3):
    num = int(input("Quick, it's important. I need an integer between 10 and 20: "))
    if 10 < num < 20:
        count += 1
print(f"You got it right {count} times")
print("\n Question 2: \n")
total = int(input("Enter a number: "))
for i in range(10):
    num = random.randint(1, 10)
    print(f"Got: {num}")
    total += num
print(f"The sum is: {total}")
print("\n Question 3: \n")
def plus_minus(N):
    s = int(input("Enter a number: "))
    for i in range(1, N + 1):
        if i % 2 == 0:
            s -= i
        else:
            s += i
    print(s)
N = 0
plus_minus(N)
print("\n Question 4: \n")
N = int(input("Give me a positive integer: "))
for i in range(1, N + 1):
    print('A' * i)
print("\n Question 5: \n")
def sq_color(x, y):
    if (x + y) % 2 == 0:
        return "black"
    else:
        return "white"
x = int(input("Enter the first coordinate (1-8): "))
y = int(input("Enter the second coordinate (1-8): "))
print(sq_color(x, y))
print("\n Question 6: \n")
N = int(input("Enter the number of lines: "))
L = int(input("Enter the length of a line: "))
colors = ["black", "red"]
t = turtle.Turtle()
for i in range(N):
    t.color(colors[i % 2])
    t.forward(L)
    t.penup()
    t.backward(L)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.pendown()
turtle.done()
