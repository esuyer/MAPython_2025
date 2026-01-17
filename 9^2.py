print("Problem 1\n")
word = input("Give me a word: ")
print("The length is:", len(word))
print("The word starts with:", word[0])
print("The word ends with:", word[-1])
print("Next to last letter:", word[-2])
print("\nProblem 2\n")
word = input("Give me a word: ")
if word[0] == word[-1]:
    print("Starts and ends with the same letter", word[0] + ".")
else:
    print("Starts and ends with different letters.")
print("\nProblem 3\n")
def add_stars(word):
    stars = "*" * len(word)
    return stars + word + stars
word = input("Give me a word: ")
print(add_stars(word))
print("\nProblem 4\n")
s = input("Give me a word with even number of letters: ")
half = len(s) // 2
print(s[half:] + s[:half])
print("\nProblem 5\n")
def ends_with_at(word):
    return word[-2:] == "at"
word = input("Give me a word: ")
print(ends_with_at(word))
print("\nProblem 6\n")
def letter_snatcher(word):
    while word != "":
        print(word)
        word = word[:-1]
word = input("Give me a word: ")
letter_snatcher(word)
