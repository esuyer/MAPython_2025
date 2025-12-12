print("Question 1\n")
def make_fish():
    print('<o))))><')

make_fish()
make_fish()

print("\n Question 2 \n")
def say_it(sentence):
    print(sentence)

sentence = input("Enter a sentence for the parrot to repeat: ")
say_it(sentence)
sentence = input("Enter another sentence: ")
say_it(sentence)
sentence = input("Enter one more sentence: ")
say_it(sentence)
print("\n Question 3 \n")
def tale(weight):
    print(f'I once caught a fish that weighed {weight} pounds')

weight = int(input("Enter the weight of the fish: "))
tale(weight)
weight = int(input("Enter another weight of a fish: "))
tale(weight)
print("\n Question 4 \n")
def n_power_n(N):
    if N > 100:
        print("Too much work")
    else:
        print(N**N)

N = int(input("Enter a number for N^N calculation: "))
n_power_n(N)
N = int(input("Enter another number for N^N calculation: "))
n_power_n(N)
print("\n Question 5 \n")
def make_it_big(N):
    return N * 1000000

N = int(input("Enter a number to make it big: "))
print(make_it_big(N))
N = int(input("Enter another number to make it big: "))
print(make_it_big(N))
print("\n Question 6 \n")
def triangle_area(height, base):
    return height * base / 2

height = int(input("Enter triangle height: "))
base = int(input("Enter triangle base: "))
print(triangle_area(height, base))

height = int(input("Enter another triangle height: "))
base = int(input("Enter another triangle base: "))
print(triangle_area(height, base))
print("\n Question 7 \n")
def many_fishes(number):
    for _ in range(number):
        print('<o))))><')

number = int(input("How many fishes do you want to print? "))
many_fishes(number)
print("\n Question 8 \n")
def bigger(A, B):
    if A >= B:
        return A
    else:
        return B

A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
print(bigger(A, B))
A = int(input("Enter another first number: "))
B = int(input("Enter another second number: "))
print(bigger(A, B))

