print("Question 1\n")
x = int(input("Give me an integer between 10 and 20: "))
if x >= 10 and x <= 20:
    print("Thank you")
else:
    print("That is not what I wanted")
print("\n Question 2 \n")
A = int(input("A = "))
B = int(input("B = "))
if A + B == 50 or A * B == 100:
    print(A, "and", B, "are a good pair")
else:
    print(A, "and", B, "are NOT a good pair")
print("\n Question 3 \n")
month = input("What is the month? ")
day = int(input("What is the day? "))
if month == "October" and day == 31:
    print("BOO!")
elif month == "November" and day == 26:
    print("Gobble, gobble!")
else:
    print("A nice day!")
print("\n Question 4 \n")
a = int(input("Give me an integer: "))
b = int(input("Give me another integer: "))
if (a > 0 and b > 0) or (a < 0 and b < 0):
    print("Same sign")
else:
    print("NOT the same sign")
print("\n Question 5 \n")
N = int(input("N = "))
r = N % 10
if r <= 2 or r >= 8:
    print("Close")
else:
    print("Far")
print("\n Question 6 \n")
X = int(input("X = "))
Y = int(input("Y = "))
if X == Y or X + Y == 9:
    print(f"The square {X},{Y} is on the big diagonal")
else:
    print(f"The square {X},{Y} is NOT on the big diagonal")
