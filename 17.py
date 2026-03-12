
print("Part a) Sequence from 10 to 100, stepping by 5:")
num = 10
while num <= 100:
    print(num)
    num += 5

print("\nPart b) Descending integers from a to b:")
a = int(input("Enter integer a (the larger number): "))
b = int(input("Enter integer b (the smaller number): "))

while a >= b:
    print(a)
    a -= 1
