import turtle
print("Question 1")
print("")
def madlib(name, interger, noun):
  print("congrats to", name, "who won #", interger, "in", noun, "contest")
madlib("Luke", 1, "super smash bros")
print("")
print("Question 2")
print("")
def cirA(radius):
  print("The area of the circle is", 3.14*r*r)
r = int(input("Enter the radius of the circle: "))
cirA(1)
print("")
print("Question 3")
print("")
def LuckNum(A, B):
  A=int(input("Enter a number: "))
  B=int(input("Enter another number: "))
  if A==7 or B==7:
    print("true")
  elif A+B==7:
    print("true")
  else:
    print("false")
LuckNum(1, 2)
print("")
print("Question 4")
print("")
print("a)")
print("a" * 5)
s="hi"
print(s*10)
print("b)")
def Rectangle(w, h):
  w=int(input("Enter the width: "))
  h=int(input("Enter the height: "))
  for i in range(h):
    print("A"*w)
Rectangle(1, 2)
print("")
print("Question 5")
print("")
X=int(input("Enter a numbers: "))
Y=int(input("Enter another number: "))
Z=int(input("Enter another number: "))
def is_triangle(A, B, C):
  return A+B>C and A+C>B and B+C>A
print(is_triangle(X, Y, Z))
print("")
print("Question 6")
print("")
print("a)")
print("on VNC")
pen=turtle.Turtle()
pen.speed(0)
pen.circle(50)
print ("b)")
Num_petals=int(input("Enter the number of petals: "))
def flower(Num_petals):
  pen=turtle.Turtle()
  pen.speed(0)
  angle=360/Num_petals
  for _ in range(Num_petals):
    pen.circle(50)
    pen.left(angle)
flower(Num_petals)
turtle.done()