from re import S


print("Question 1")
print("")
x= input("Give me a word")
print("The length of the word is:",len(x))
print("The last letter is:",x[-1])
print("The first letter is:",x[0])
print("The second to last letter is:",x[-2])
print("")
print("Question 2")
print("")
y= input("Give me a word")
if y[0]==y[-1]:
  print("The first and last letter are the same")
else:
  print("The first and last letter are not the same")
print("")
print("Question 3")
print("")
a= input("Give me a word")
length= len(a)
def add_stars(a):
     stars = "*"*length
     return stars + a + stars
print(add_stars(a))
print("")
print("Question 4")
print("")
b= input("Give me a word that has an even amount of characters")
half_string= len(b)//2
print(b[half_string:]+b[:half_string])
print("")
print("Question 5")
print("")
def at_end(c):
  return c[-2:] == "at"
c= input("Give me a word")
print(at_end(c))
print("")
print("Question 6")
print("")
def letter_snatch(d):
  while d!="":
    print(d)
    d= d[:-1]
d=input("Give me a word")
letter_snatch(d)