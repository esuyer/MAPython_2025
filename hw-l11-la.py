import time

def addstars(word):
  return "*" * str.__len__() + str + "*" * str.__len__()

str = "e"
while str.__len__() < 2:
  str = input("give me a word thats has at least 2 letters: ")
  if str.__len__() < 2:
    print("retry")
    time.sleep(1)
print("the length of", str, "is", str.__len__())
time.sleep(1)
print("the first letter of", str, "is", str[0])
time.sleep(1)
print("the last letter of", str, "is", str[-1])
time.sleep(1)
print("and the 2nd last letter of", str, "is", str[-2])
time.sleep(3)

print("next")
time.sleep(1)

str = input("give me a word")
if str[0] == str[-1]:
  print(str, "starts and ends with", str[0])
else:
  print(str, "do not end with the same letter")
time.sleep(2)

print("next")
time.sleep(1)

str = input("give me a word: ")
print(str, "+ stars =", addstars(str))
time.sleep(2)

print("next")
time.sleep(1)

print("uh")
time.sleep(0.1)

print("next")
time.sleep(1)

str = "e"
while str.__len__() < 2:
  str = input("give me a word thats has at least 2 letters: ")
  if str.__len__() < 2:
    print("retry")
    time.sleep(1)
if str[-2:-1] == "at":
  print("the last 2 letters of", str, "are at")
else:
  print("the last 2 letters of", str, "are not at")
