value = int(input("Give me a number between 1 and 12:"))
if value >= 12:
    print("Dozen!")
else:
    print("Not a dozen!")
    
temperature = int(input("What is the temperature?"))
if temperature <= 32:
    print("It’s freezing!")
else:
    print("I’m going outside!")

day = input("Give me a number between 1 and 7:")
if day == 1:
    print("Sunday")
elif day == 7:
    print("Saturday")
else:
    print("Not weekend")

N = int(input("Give me a number:"))
if N % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

N = int(input("Give me a number:"))
if N % 2 == 0:
    print("even")
else:
    print("odd")

X = int(input("How much money does Alice have?"))
Y = int(input("How much money does Joe have?"))
print("Alice has", X, "dollars")
print("Joe has", Y, "dollars")
if X + Y >= 20:
    print("Buying cake!")
else:
    print("Not enough money.")
