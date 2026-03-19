print("Question 1\n")
s = input("Give me a string: ")

if 'a' in s:
    pos = s.index('a')
    print(s[pos+1:])
else:
    print("") 


print("Question 2\n")
def combination_lock(N):
    s = str(N)

    if len(s) != 6:
        return False

    if s[0] != s[-1]:
        return False

    if int(s[3]) % 2 != 0:
        return False

    if int(s[4]) + int(s[5]) != 10:
        return False

    return True

num = int(input("Enter a number for the lock: "))
print(combination_lock(num))


print("Question 3\n")
first_names = input("Enter first names separated by space: ").split()
last_names = input("Enter last names separated by space: ").split()

full_names = []

length = min(len(first_names), len(last_names))

for i in range(length):
    full_names.append(first_names[i] + " " + last_names[i])

print(full_names)


print("Question 4\n")
def decode_caesar(message, shift):
    result = ""

    for ch in message:
        if ch.isalpha():
            new_char = chr(ord(ch) - shift)

            if ch.islower() and new_char < 'a':
                new_char = chr(ord(new_char) + 26)
            elif ch.isupper() and new_char < 'A':
                new_char = chr(ord(new_char) + 26)

            result += new_char
        else:
            result += ch

    return result

msg = input("Enter encoded message: ")
shift = int(input("Enter shift: "))
print(decode_caesar(msg, shift))


print("Question 5\n")
def decode_spy(message):
    n = len(message)

    first_half_len = (n + 1) // 2
    second_half_len = n // 2

    first_half = ""
    second_half = ""

    for i in range(n):
        if i % 2 == 0:
            first_half += message[i]
        else:
            second_half += message[i]

    return first_half + second_half

encoded = input("Enter encoded spy message: ")
print(decode_spy(encoded))
