print("Question 1\n")
a = 0
b = 5
c = 5
while a <= 10:
    print(a)
    a = a + 1
print("\nQuestion 2\n")
while b <= 12:
   print(b)
   b = b + 1
print("\nQuestion 3\n")
while c >= -5:
   print(c)
   c = c - 1
print("\nQuestion 4\n")
d = int(input("Give me a number less than 50: "))
while d <= 50:
   print(d)
   d = d + 2
print("\nQuestion 5\n")
e = int(input("Give me a positive number: "))
while e > 0:
   print(e)
   e = e - 3
print("\nQuestion 6\n")
f = int(input("Give me a number: "))
g = int(input("Give me a bigger number: "))
while f < g:
   print(f)
   f = f + 1
print("\nQuestion 7\n")
words = ['head', 'body', 'tail']
print(words)
g = 0
while g < len(words):
    print(words[g])
    g += 1
print("\nQuestion 8\n")
print(words)
h = len(words)
while h > 0:
    h -= 1
    print(words[h])
print("\nQuestion 9\n")
i = int(input("Give me a positive integer: "))
j = 1
while j * j < i:
    print(j * j)
    j += 1
print("\nQuestion 10\n")
k = int(input("Give me a positive integer: "))
ll = 1
while 2 ** ll < k:
    print(2 ** ll)
    ll += 1
print("\nQuestion 11\n")
m = int(input("Give me an integer: "))
n = 0
o = 1
p = 0
q = 0
while n <= m:
    p = n
    q = o - 1
    n += o
    o += 1
print("First sum over the limit:", n)
print("Last sum not over the limit:", p)
print("Last number added:", q)
print("\nQuestion 12\n")
r = int(input("Give me a positive integer: "))
def smallest_div(r):
    s = 2
    while s <= r:
        if r % s == 0:
            return s
        s += 1
print(smallest_div(17))
print(smallest_div(123456))
print(smallest_div(35))