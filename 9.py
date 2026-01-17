print("Enter your name: ")
s = input()
print(s)
print(s[len(s) - 1])
print(s[-1])
print("Contains t" if 't' in s else "Does not contain t")
print("Enter your first name: ")
def initials(first_name, last_name):
    return first_name[0] + last_name[0]

first = input()
print("Enter your last name: ")
last = input()
print(initials(first, last))
print("Enter a number: ")
def ends(text):
    return text[0] + text[-1]

print(ends(input()))
print("Enter two numbers: ")
def stars_pluses(a, b):
    return "*" * a + "+" * b
a = int(input())
b = int(input())
print(stars_pluses(a, b))
print("Enter your name: ")
name = input()
print(name[:3])
print(name[-5:])
print(name[8:11])
print("Enter a string: ")
def first_two(text):
    return text[:2]

print(first_two(input()))
print("Enter a string: ")
def first_half(text):
    return text[:len(text)//2]

print(first_half(input()))
print("Enter a string: ")
def without_ends(text):
    return text[1:-1]

print(without_ends(input()))
