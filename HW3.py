import random
import turtle


def problem1():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    print(num1)
    print(num2)
    print("Sum =", num1 + num2, "Difference =", num1 - num2)


def problem2():
    count = int(input("How many smileys do you want? "))
    for i in range(count):
        print(":)")


def problem3():
    rolls = int(input("How many times should I roll the die? "))
    for i in range(rolls):
        print("Rolled", random.randint(1, 6))


def problem4():
    t = turtle.Turtle()
    t.speed(5)
    for i in range(5):
        side = random.randint(50, 200)
        for j in range(3):
            t.forward(side)
            t.left(120)
        t.penup()
        t.forward(side + 20)
        t.pendown()
    turtle.done()


def problem5():
    t = turtle.Turtle()
    t.speed(5)
    num = random.randint(1, 10)
    print(num)
    for i in range(num):
        for j in range(4):
            t.forward(50)
            t.right(90)
        t.penup()
        t.forward(70)
        t.pendown()
    turtle.done()


def problem6():
    t = turtle.Turtle()
    t.speed(5)
    for i in range(6):
        t.forward(100)
        t.left(60)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    for i in range(6):
        t.forward(100)
        t.right(60)
    turtle.done()


while True:
    print("1. Random numbers")
    print("2. Smiley")
    print("3. Rolling a die")
    print("4. Triangles")
    print("5. Square pattern")
    print("6. Draw only once")
    print("0. Exit")
    choice = input("Choose a problem: ")
    if choice == "1":
        problem1()
    elif choice == "2":
        problem2()
    elif choice == "3":
        problem3()
    elif choice == "4":
        problem4()
    elif choice == "5":
        problem5()
    elif choice == "6":
        problem6()
    elif choice == "0":
        break
    else:
        print("Invalid choice")
