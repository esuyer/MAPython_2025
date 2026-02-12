import random

print("Problem 1")
print()
colors = []
nouns = []
adjs = []

for i in range(3):
    colors.append(input("Enter a color: "))
for i in range(3):
    nouns.append(input("Enter a noun: "))
for i in range(3):
    adjs.append(input("Enter an adjective: "))

for i in range(5):
    c = random.choice(colors)
    n = random.choice(nouns)
    a = random.choice(adjs)
    print("I got a", c, n, "for the New Year. It was", a)

print()
print("Problem 2")
print()
words = input("Enter words separated by spaces (must include 'cart'): ").split()
print("Before:", words)
i = words.index("cart")
words.insert(i, "horse")
print("After:", words)

print()
print("Problem 3")
print()
lst = input("Enter at least 5 words separated by spaces: ").split()
print("List:", lst)

if "dust" in lst:
    lst.remove("dust")
print("a):", lst)

removed3 = lst.pop(2)
print("b) Removed 3rd:", removed3)
print(lst)

removed_last = []
for i in range(3):
    removed_last.append(lst.pop())
print("c) Removed last 3:")
for item in removed_last:
    print(item)
print(lst)

print()
print("Problem 4")
print()
nums = list(map(int, input("Enter positive integers separated by spaces: ").split()))
new_list = []
for n in nums:
    new_list.append("+" * n)
print("Original list:", nums)
print("New list:", new_list)

print()
print("Problem 5")
print()
def horse_before_cart2(original):
    new = []
    for word in original:
        if word == "cart":
            new.append("horse")
        new.append(word)
    print("Original list:", original)
    print("New list:", new)

words2 = input("Enter words separated by spaces (may include several 'cart'): ").split()
horse_before_cart2(words2)

print()
print("Problem 6")
print()
def find_max(line):
    if "Max" not in line:
        print("Max is not in line")
    else:
        i = line.index("Max")
        print("Max is number", i + 1, "in line")
        if i == 0:
            print("There is no one in front of him")
        else:
            print(line[i-1], "is in front of him")
        if i == len(line) - 1:
            print("There is no one behind him")
        else:
            print(line[i+1], "is behind him")

line = input("Enter names separated by spaces: ").split()
find_max(line)