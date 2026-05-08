print("Question 1")
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

print("\nQuestion 2")
nums_input = input("Enter integers separated by commas: ")
nums = nums_input.split(",")
print(nums)
total = int(nums[0]) + int(nums[-1])
print("Sum of first and last:", total)
