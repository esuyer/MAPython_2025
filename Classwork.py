import random

# Problem 1
def after3_encode(message):
    encoded = ""
    count = 0

    for ch in message:
        encoded += ch
        count += 1

        if count % 3 == 0:
            encoded += "the"

    return encoded


# Problem 2
def after3_random_encode(message):
    words = ["the", "cat", "was", "fat", "sun", "sky", "dog"]
    encoded = ""
    count = 0

    for ch in message:
        encoded += ch
        count += 1

        if count % 3 == 0:
            encoded += random.choice(words)

    return encoded


# Problem 3
def split_encode(message):
    even = ""
    odd = ""

    for i in range(len(message)):
        if i % 2 == 0:
            even += message[i]
        else:
            odd += message[i]

    return even + odd


# Problem 4
def flip_encode(message):
    if len(message) % 2 != 0:
        return "Error: message must have even length."

    encoded = ""

    for i in range(0, len(message), 2):
        encoded += message[i+1] + message[i]

    return encoded


# Ask user for a message
msg = input("Enter a message: ")

print("\nProblem 1 result:")
print(after3_encode(msg))

print("\nProblem 2 result:")
print(after3_random_encode(msg))

print("\nProblem 3 result:")
print(split_encode(msg))

print("\nProblem 4 result:")
print(flip_encode(msg))