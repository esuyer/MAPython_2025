import random
i = 10
while i <= 100:
    print(i)
    i += 5

a = int(input("Give me an integer: "))
b = int(input("Give me a smaller integer: "))
while a >= b:
    print(a)
    a -= 1

total = 0
print("total=", total)
while total <= 50:
    n = int(input("Give me a number and I will add it to the total: "))
    total += n
    print("total=", total)
    if total > 50:
        print("That was over 50, too hard. Stopping now!")

def swap_ao(S):
    result = ""
    for ch in S:
        if ch == "a":
            result += "o"
        elif ch == "o":
            result += "a"
        else:
            result += ch
    return result

def add_dots(S):
    result = ""
    for ch in S:
        result += "." + ch
    return result

print(swap_ao("baobab"))
print(add_dots("dots"))


while True:
    r = random.randint(1,6)
    print("Rolled:", r)
    if r > 4:
        break

total = 0
print("total weight =", total)
while True:
    w = int(input("What is the weight of the next item to pack? "))
    if total + w > 25:
        print("That would be over the limit of 25 lbs, can't add that. Stopping now!")
        break
    total += w
    print("Item added. Total weight =", total)
print("Your final suitcase weight =", total)