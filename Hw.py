# Problem 1. Suitable names
def puppy_names(names):
    count = 0

    for name in names:
        name = name.strip()
        if len(name) <= 5:
            print(name)
            count += 1

    print("There were", count, "suitable names.")

user_names = input("Enter dog names separated by commas: ").split(",")
puppy_names(user_names)


# Problem 2. Not first, not last
lst = input("Enter elements separated by space: ").split()

for i in range(1, len(lst) - 1):
    print(lst[i])


# Problem 3. Count, search, add
def list_info(numbers):
    count = 0
    has_negative = False
    odd_sum = 0

    for num in numbers:
        if 0 < num < 100:
            count += 1

        if num < 0:
            has_negative = True

        if num % 2 != 0:
            odd_sum += num

    print("There are", count, "numbers between 0 and 100")

    if has_negative:
        print("There is a negative number in the list")
    else:
        print("There are no negative numbers in the list")

    print("The sum of odd numbers is", odd_sum)

nums = list(map(int, input("Enter numbers separated by space: ").split()))
list_info(nums)


# Problem 4. Test scores
scores = list(map(int, input("Enter test scores separated by space: ").split()))

all_passed = True

for score in scores:
    if score < 100:
        all_passed = False
        break

if all_passed:
    print("Everyone passed.")
else:
    print("Not everyone passed.")


# Problem 5. Starts with z
words = input("Enter words separated by space: ").split()

found = False

for word in words:
    if word.startswith('z'):
        found = True
        break

print(found)