def from_first(words):
    result = ""
    for word in words:
        result = result + word[0]
    return result

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
word3 = input("Enter third word: ")

print(from_first([word1, word2, word3]))
