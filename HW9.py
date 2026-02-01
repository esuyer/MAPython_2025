import os
# Audio fix for turtle/headless environments
os.environ['SDL_AUDIODRIVER'] = 'dummy'
import turtle

print("Problem 1\n")
nums = []
for _ in range(5):
    nums.append(int(input("Give me a number: ")))

print("First plus last: ", nums[0] + nums[-1])
for n in nums:
    print(n)

print("Odd numbers only: ")
for n in nums:
    if n % 2 == 1:
        print(n)

print("\nProblem 2\n")
friends = []
f_count = int(input("How many friends do you want to invite: "))
for _ in range(f_count):
    name = input("Enter a name: ")
    friends.append(name)
print(friends)

print("\nProblem 3\n")
multi = []
h = int(input("Give me a number: "))
for i in range(h):
    multi.append("*" * (i + 1))
print(multi)

print("\nProblem 4\n")
print("Enter 4 pokemon for Jake:")
jake = [input(f"Jake's pokemon {i+1}: ") for i in range(4)]
print("\nEnter 4 pokemon for Andrew:")
andrew = [input(f"Andrew's pokemon {i+1}: ") for i in range(4)]

print("Jake's pokemon: ", jake)
print("Andrew's pokemon: ", andrew)
print("Different pokemon in Jake's list compared to Andrew's at same index: ")
for i in range(len(jake)):
    if jake[i] != andrew[i]:
        print(jake[i])

print("\nProblem 5\n")
colours = []
q = int(input("How many colours do you want to enter: "))
for i in range(q):
    r = input("Enter a colour: ")
    colours.append(r)

# Setup turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

for c in colours:
    t.color(c)
    t.forward(100)
    t.stamp()

print("\nDone! Close the turtle window to finish.")
turtle.done()
