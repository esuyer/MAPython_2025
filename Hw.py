word = input("Give me a word: ")
if word[0].lower() == word[-1].lower():
    print("Starts and ends with the same letter", word[0].lower())
else:
    print("Starts and ends with different letters")
print(word.upper())

c1 = input("Give me a single character: ")
c2 = input("Give me another single character: ")
if c1 == c2:
    print("That is the same character")
elif c1 < c2:
    print(c1, "comes before", c2)
else:
    print(c2, "comes before", c1)

def vowels_to_pluses(S):
    result = ""
    for ch in S:
        if ch in "aeiouAEIOU":
            result += "+"
        else:
            result += ch
    return result

def double_letters(S):
    result = ""
    for ch in S:
        result += ch + ch
    return result

def remove_even(S):
    result = ""
    for i in range(len(S)):
        if i % 2 == 0:
            result += S[i]
    return result

def case(S):
    if S.isupper():
        print("All uppercase")
    elif S.islower():
        print("All lowercase")
    else:
        print("Mix")

S = input("Give me a string: ")

print(vowels_to_pluses(S))
print(double_letters(S))
print(remove_even(S))
case(S)