# Problem 1. After first 'a'
s = input("Give me a string: ")

if 'a' in s:
    pos = s.index('a')
    print(s[pos+1:])
else:
    print("")  # print nothing


# Problem 2. Combination lock
def combination_lock(N):
    s = str(N)

    # Must be 6 digits
    if len(s) != 6:
        return False

    # 1st and last digits same
    if s[0] != s[-1]:
        return False

    # 4th digit is even (index 3)
    if int(s[3]) % 2 != 0:
        return False

    # 5th + 6th digits = 10
    if int(s[4]) + int(s[5]) != 10:
        return False

    return True

num = int(input("Enter a number for the lock: "))
print(combination_lock(num))


# Problem 3. Full names
first_names = input("Enter first names separated by space: ").split()
last_names = input("Enter last names separated by space: ").split()

full_names = []

length = min(len(first_names), len(last_names))

for i in range(length):
    full_names.append(first_names[i] + " " + last_names[i])

print(full_names)


# Problem 4. Caesar cipher decoding
def decode_caesar(message, shift):
    result = ""

    for ch in message:
        if ch.isalpha():
            # shift LEFT
            new_char = chr(ord(ch) - shift)

            # wrap around if needed
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


# Problem 5. Decode alternating halves
def decode_spy(message):
    n = len(message)

    # split lengths
    first_half_len = (n + 1) // 2
    second_half_len = n // 2

    first_half = ""
    second_half = ""

    # extract alternating characters
    for i in range(n):
        if i % 2 == 0:
            first_half += message[i]
        else:
            second_half += message[i]

    return first_half + second_half

encoded = input("Enter encoded spy message: ")
print(decode_spy(encoded))