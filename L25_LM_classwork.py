names_input = input("Enter names separated by spaces: ")
names = names_input.split(" ")
print(names)

if len(names) >= 2:
    if names[1] == "Bob":
        print("The second name is Bob")
    else:
        print("The second name is not Bob")
else:
    print("There is no second name")
