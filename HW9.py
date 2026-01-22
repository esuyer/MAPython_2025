print("Problem 1")
word = input("Give me a word: ")
for letter in word:
    print(letter)

print("Problem 2")
word = input("Give me a word: ")
for letter in word:
    print(letter * 5)

print("Problem 3")
word = input("Give me a word: ")
vowels = "aeiou"
count = 0
for letter in word:
    if letter in vowels:
        print(letter)
        count += 1
print(count, "vowels")

print("Problem 4")
word = input("Give me a word: ")
vowels = "aeiou"
for letter in word:
    if letter not in vowels:
        print(letter)

print("Problem 5")
word = input("Give me a word: ")
for letter in word:
    if letter == 'a':
        print('z')
    else:
        print(letter)

print("Problem 6")
word = input("Give me a word: ")
for i in range(len(word)):
    if i % 2 == 0:
        print(word[i])
    else:
        print('*')

print("Problem 7")
word = input("Give me a word: ")
for i in range(len(word)):
    print(word[i] * (i + 1))

print("Problem 8")
word = input("Give me a word: ")
for letter in word[::-1]:
    print(letter)
