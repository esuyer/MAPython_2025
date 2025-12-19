import turtle
print("Question 1\n")
def madlib(name, integer, noun):
  print(f"Congrats to {name} who won place # {integer} in the {noun} contest.")
name = input("Enter a name: ")
integer = int(input("Enter a number: "))
noun = input("Enter a noun: ")
madlib(name, integer, noun)
print("\n Question 2 \n")
radius = int(input("Enter circle radius: "))
def circle_area(radius):
  pi = 3.14
  return pi * radius ** 2
print(circle_area(radius))
print("\n Question 3 \n")
a = int(input("Enter first number for lucky 7: "))
b = int(input("Enter second number for lucky 7: "))
def got_7(a, b):
  return a == 7 or b == 7 or (a + b) == 7 or abs(a - b) == 7
print(got_7(a, b))
print("\n Question 4 \n")
width = int(input("Enter rectangle width: "))
height = int(input("Enter rectangle height: "))
def rectangle_pattern(width, height):
  for _ in range(height):
      print("A" * width)
rectangle_pattern(width, height)
print("\n Question 5 \n")
x = int(input("Enter first side of triangle: "))
y = int(input("Enter second side of triangle: "))
z = int(input("Enter third side of triangle: "))
def is_triangle(a, b, c):
  return a + b > c and a + c > b and b + c > a
print(is_triangle(x, y, z))
print("\n Question 6 \n")
num_petals = int(input("Enter number of petals for flower: "))
def flower(num_petals):
  pen = turtle.Turtle()
  pen.speed(0)
  angle = 360 / num_petals
  for _ in range(num_petals):
      pen.circle(50)
      pen.left(angle)
  turtle.done()
flower(num_petals)
