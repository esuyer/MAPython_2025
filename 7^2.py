print("Question 1\n")
N = int(input("Give me an integer: "))
for i in range(N + 1):
    if (i % 2 == 0 and i % 3 == 0) or (i % 2 == 1 and i % 5 == 0):
        print(i)
print("\n Question 2 \n")
d1 = int(input("Enter a number:"))
d2 = int(input("Enter another number:"))
if d1 == 1 or d2 == 1:
    print("do not buy")
elif d1 == 4 or d2 == 4:
    print("buy")
else:
    print("need time to think")
print("\n Question 3 \n")
row1 = int(input("Enter a number:"))
col1 = int(input("Enter another number:"))
row2 = int(input("Enter a number:"))
col2 = int(input("Enter another number:"))
if (abs(row1 - row2) == 1 and col1 == col2) or (abs(col1 - col2) == 1 and row1 == row2):
    print(True)
else:
    print(False)
print("\n Question 4 \n")
N = int(input())
outside_mode = input() == "True"
if not outside_mode:
        print(1 <= N <= 10)
else:
        print(N < 1 or N > 10)
print("\n Question 5 \n")
A = int(input("Enter a number:"))
B = int(input("Enter another number:"))
C = int(input("Enter another number:"))
if A % 10 == B % 10 or A % 10 == C % 10 or B % 10 == C % 10:
    print(True)
else:
    print(False)
