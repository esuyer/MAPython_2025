
print("problem 1")
str1 = "winter"
print(str1[0])
print(str1[2])
print(str1[len(str1)-1])
if ("t" in str1)  :
  print("Yes, 't' is present.")


print("problem 2")
def initials(first_name, last_name):
   return first_name[0] + last_name[0]

print(initials("Sherlock", "Holmes"))

print("problem 3")
def ends(word):
   return word[0] + word[len(word)-1]

print(ends("winter"))

print("problem 4")
def stars(s, p) :
  result = ""
  for i in range(0, s): 
    result+="*"
  for i in range(0, p): 
    result+="+"

  return result

print(stars(5,4))



