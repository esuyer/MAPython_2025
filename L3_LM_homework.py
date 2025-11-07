import turtle
print("Question 1")
print("")
random=__import__("random")
ran_num1=random.randint(1,10)
ran_num2=random.randint(1,10)
print(ran_num1,ran_num2)
print(ran_num1+ran_num2)
print(ran_num1-ran_num2)
print("Question 2")
print("")
smile=int(input("How many smiley faces do you want?"))
for i in range(smile):
    print("\U0001f600")
print("Question 3")
print("")
dice=(input("how many times do you want to roll the dice?"))


for i in range(5):
    random_number = random.randint(1, 6)
    print(f"Random number {i+1}: {random_number}")
print("Question 4")
print("")
t= turtle.Turtle()
t.speed(5)
for i in range(5):
    side=random.randint(50,200)
    for j in range(5):
        t.forward(side)
        t.left(120)

turtle.done()