print("Question 1")
print("")
my_string = "Hello, World!"
print(my_string)
print(my_string[3])
print(my_string[12])
if "t" in  my_string:
  print("contains t")
else:
  print("does not contain t")
print("")
print("Question 2")
print("")
def initials(first_name, last_name):
  print(first_name[0]+last_name[0])
initials("Luke", "Marjault")
print("")
print("Question 3")
print("")
str3 = "Hello"
print(str3[3:5])
print("")
print("Question 4")
print("")
def star_pluses(a, b):
  result = ""
  for i in range(a):
     result += "*"
  for i in range(b):
     result += "+"
  return result
print(star_pluses(4, 2))
print("")
print("Question 5")
print("")
str4= "Bobby Brown"
print(str4[0:3])
print(str4[6:11])
print(str4[7:10])
print("")
print("Question 6")
print("")