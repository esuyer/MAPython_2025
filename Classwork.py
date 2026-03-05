print("Question 1\n")
a = input("Type anything: ")
a = a.replace("a", "z")
a = a.replace("A", "z")
print(a)
print("\nQuestion 2\n")
c = input("Type anything: ")
def even_to_dot(c):
  result = ""
  i = 0
  for letter in c:
      if i % 2 == 0:
          result += "."
      else:
          result += letter
      i += 1
  return result
print(even_to_dot(c))
print("\nQuestion 3\n")
d = input("Type anything: ")
def remove_aA(d):
         result = ""
         for letter in d:
             if letter != "a" and letter != "A":
                 result += letter
         return result
print(remove_aA(d))
print("\nQuestion 4\n")
e = input("Type anything: ")
def upper_lower(e):
  result = ""
  for i in range(len(e)):
      if i % 2 == 0:
          result += e[i].upper()
      else:
          result += e[i].lower()
  return result
print(upper_lower(e))
print("\nQuestion 5\n")
f = input("Type anything: ")
def before_m(f):
  result = ""
  for letter in f:
      if letter >= "m":
          result += letter
  return result
print(before_m(f))
print("\nQuestion 6\n")
S = input("Type anything: ")
N = int(input("Type a number: "))
def up_at_pos(S, N):
    result = ""
    for i in range(len(S)):
        if i == N:
            result += S[i].upper()
        else:
            result += S[i].lower()
    return result
print(up_at_pos(S, N))
print("\nQuestion 7\n")
i1 = input("Type anything: ")
j = int(input("Type a number: "))
def mul_str(i1, j):
  result = ""
  for i in range(j):
      result += i1
  return result
print(mul_str(i1, j))
print("\nQuestion 8\n")
k = input("Type anything: ")
def reverse(k):
  result = ""
  for letter in k:
      result = letter + result
  return result
print(reverse(k))