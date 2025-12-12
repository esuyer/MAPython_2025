import turtle
print("Problem 9: Aircraft warning system")
left_gear = input("Is the left gear up? (True/False): ") == "True"
right_gear = input("Is the right gear up? (True/False): ") == "True"
def same_pos(left_gear, right_gear):
    return left_gear == right_gear
print(same_pos(left_gear, right_gear))

print("Problem 10: Square")
def draw_square(side, color):
    t = turtle.Turtle()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(side)
        t.right(90)
    t.end_fill()
    t.hideturtle()
side1 = int(input("Enter side length of first square: "))
color1 = input("Enter color of first square: ")
side2 = int(input("Enter side length of second square: "))
color2 = input("Enter color of second square: ")
draw_square(side1, color1)
draw_square(side2, color2)

print("Problem 11: Pool")
def pool(W, L, x, y):
    print(min(x, W - x, y, L - y))
W = int(input("Enter pool width W: "))
L = int(input("Enter pool length L: "))
x = int(input("Enter distance x from short side: "))
y = int(input("Enter distance y from long side: "))
pool(W, L, x, y)

print("Problem 12: Chocolate bar")
def chocolate_bar(M, N, K):
    print(K <= M * N and (K % M == 0 or K % N == 0))
M = int(input("Enter chocolate bar rows M: "))
N = int(input("Enter chocolate bar columns N: "))
K = int(input("Enter number of sections K: "))
chocolate_bar(M, N, K)

turtle.done()
