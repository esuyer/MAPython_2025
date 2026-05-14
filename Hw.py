words = input("Give me several words separated by spaces: ").split()
print(words)
if "rain" in words:
    print("Found rain")
else:
    print("Did not find rain")

nums = input("Give me several integers separated by commas: ").split(",")
for n in nums:
    n = int(n)
    print("+" * n)

def robot(command):
    parts = command.split()
    word = parts[0]
    times = int(parts[1])
    for _ in range(times):
        print(word)

s = input("Give me a string: ")
freq = {}
for c in s:
    if c not in freq:
        freq[c] = 1
    else:
        freq[c] += 1
print(freq)

def get_password(message):
    words = message.split()
    password = ""
    for w in words:
        password += w[0]
    return password