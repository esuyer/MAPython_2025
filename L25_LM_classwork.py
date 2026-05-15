print("Question 1\n")
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

print("\nQuestion 2\n")
nums_input = input("Enter integers separated by commas: ")
nums = nums_input.split(",")
print(nums)
total = int(nums[0]) + int(nums[-1])
print("Sum of first and last:", total)

print("\nQuestion 3\n")
def print_words(sentence):
    words = sentence.split(" ")
    print("Number of words:", len(words))
    for word in words:
        print(word)

sentence = input("Enter words separated by spaces: ")
print_words(sentence)

print("\nQuestion 4\n")
nums_input = input("Enter integers separated by commas: ")
nums = nums_input.split(",")
for num in nums:
    if int(num) < 10:
        print(num)

print("\nQuestion 5\n")
def check_sum(nums_str):
    nums = nums_str.split(" ")
    a = int(nums[0])
    b = int(nums[1])
    c = int(nums[2])
    return a + b == c

user_input = input("Enter 3 integers separated by spaces: ")
print(check_sum(user_input))

print("\nQuestion 6\n")