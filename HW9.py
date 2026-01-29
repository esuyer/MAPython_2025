def problem1():
    print("Problem 1")
    print()
    word = input("Give me a word: ")
    for c in word:
        if c == 'a' or c == 'A':
            print(c)

def chain(w1, w2):
    print("Problem 2")
    print()
    if w1[0] == w2[-1]:
        print(w2, w1)
    elif w2[0] == w1[-1]:
        print(w1, w2)
    else:
        print("NO CHAIN")

def problem3():
    print("Problem 3")
    print()
    w1 = input("Give me a word: ")
    w2 = input("Give me another word: ")
    if w1[-2:] == w2[-2:]:
        print(w1, "and", w2, "rhyme")
    else:
        print(w1, "and", w2, "DO NOT rhyme")

def secret_message(a, b):
    print("Problem 4")
    print()
    for i in range(len(a)):
        print(a[i])
        print(b[i])

def problem5():
    print("Problem 5")
    print()
    word = input("Give me a word: ")
    for i in range(len(word)):
        print("." * i + word[i])

problem1()
print()
chain('dog','toad')
print()
chain('cat','take')
print()
chain('cake','rat')
print()
problem3()
print()
secret_message('Pto','yhn')
print()
secret_message('fo','lp')
print()
problem5()
