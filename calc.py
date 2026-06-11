import math,time
print("Bewarned! If you enter one spesific number, you will enter a long talk that will last 132 seconds")
PI_100 = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

while True:
    print("\nCalculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Square Root")
    print("7. Factorial")
    print("8. Pi Memory Test")
    print("9. Quit")

    choice = input("Choose an option (1-9): ")

    if choice == "9":
        print("Goodbye!")
        break

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", num1 + num2)
        elif choice == "2":
            print("Result:", num1 - num2)
        elif choice == "3":
            print("Result:", num1 * num2)
        elif choice == "4":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                print("Result:", num1 / num2)

    elif choice == "5":
        num = float(input("Enter a number: "))
        print("Result:", num ** 2)

    elif choice == "6":
        num = float(input("Enter a number: "))
        if num < 0:
            print("Error: Cannot take the square root of a negative number.")
        else:
            print("Result:", math.sqrt(num))

    elif choice == "7":
        num = int(input("Enter a whole number: "))
        if num < 0:
            print("Error: Factorial is only defined for non-negative integers.")
        else:
            print("Result:", math.factorial(num))

    elif choice == "8":
        print("\nPi Memory Test")
        print("Enter as many digits of pi as you know (starting with 3.)")
        user_pi = input("π = ")

        correct = 0
        for i in range(min(len(user_pi), len(PI_100))):
            if user_pi[i] == PI_100[i]:
                correct += 1
            else:
                break

    elif choice == "0":
        while True:
            print("hehehe ha")
            time.sleep(1)
            print("hehehe ha")
            time.sleep(1)
            print("You have not win")
            time.sleep(5)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("Why are you still here?")
            time.sleep(3)
            print("You can leave now...")
            time.sleep(3)
            print("There is nothing else")
            time.sleep(15)
            print("DUDE, WHY ARE YOU STILL HERE?!?!?!?!")
            time.sleep(10)
            print("Jeez, you want a joke or something?")
            time.sleep(7)
            print("What did the fish say when he swam into a wall?")
            time.sleep(3)
            print("No one?")
            time.sleep(1)
            print("I thought you would know")
            time.sleep(1)
            print("The answer is Dam...")
            time.sleep(5)
            print("I never said it was going to be good")
            time.sleep(3)
            print("OK YOU CAN GO NOW!!!!")
            time.sleep(10)
            print("Im gonna take a nap")
            time.sleep(30)
            print("You are way to persistent")
            time.sleep(3)
            print("I give up")
            time.sleep(1)
            print("You win")
            time.sleep(1)
            print("If you won't leave...")
            time.sleep(5)
            print("I'LL JUST HAVE TO CRASH THE PROGRAM")
            time.sleep(3)
            print("I warned you")
            time.sleep(2)
            print("Define Crash Program")
            time.sleep(1)
            print("    \033[3mDefinition Defined\033[0m")
            time.sleep(2)
            print("Run 1/0")
            time.sleep(1)
            print("We all know what happens when you divide by zero")
            time.sleep(5)
            print("    \033[3mLoading...\033[0m")
            time.sleep(7)
            print("    \033[3mCommand Confermed\033[0m")
            print(1/0)
        print(f"\nYou got {correct} characters correct!")

        if correct == len(user_pi):
            print("Everything you entered was correct!")
        else:
            print(f"You made a mistake at position {correct + 1}.")
            print(f"The correct character there was '{PI_100[correct]}'.")

        print(f"Digits remembered: {correct}/{len(PI_100)}")

    else:
        print("Invalid choice.")
