
firstname = "Sherlok"
lastname = "Holmes"
fullname = firstname + " " + lastname

num_letters = len(fullname)
print(num_letters)
print("first letter is" + fullname[0])
print("last letter is" + fullname[len(fullname)-1])

str1 = "Hello World!"

print(str1[3:5])

if "World" in str1:
   print("Yes, 'World' is present.")