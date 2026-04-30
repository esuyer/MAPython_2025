from multiprocessing.resource_sharer import stop
import turtle
import random
print("Question 1\n")
screen = turtle.Screen()
screen.title("Left and Right Click Counters")
screen.bgcolor("white")

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

left_count = 0
right_count = 0

def update_display():
    writer.clear()
    writer.goto(0, 50)
    writer.write("Left clicks: " + str(left_count), align="center", font=("Arial", 20, "bold"))
    writer.goto(0, 0)
    writer.write("Right clicks: " + str(right_count), align="center", font=("Arial", 20, "bold"))

def left_click(x, y):
    global left_count
    left_count += 1
    update_display()

def right_click(x, y):
    global right_count
    right_count += 1
    update_display()

screen.onclick(left_click, btn=1)
screen.onclick(right_click, btn=3)
#screen.mainloop()
print("\nQuestion 2\n")

def draw_line_and_stamp(x, y):
    r = random.random()
    g = random.random()
    b = random.random()
    pen.color(r, g, b)

    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.goto(x, y)

    pen.stamp()

screen = turtle.Screen()
screen.title("Click to Draw!")

pen = turtle.Turtle()
pen.speed(0) 
pen.shape("circle")
pen.shapesize(0.5) 

screen.onscreenclick(draw_line_and_stamp)

#turtle.mainloop()

print("\nQuestion 3\n")
def remove_letter(word, n):
    return word[:n] + word[n+1:]
    
user_word = input("Enter a word: ")
user_num = int(input("Enter the position to remove: "))

result = remove_letter(user_word, user_num)
print("Result:", result)

print("\nQuestion 4\n")
def check_word_for_sue(word):
    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            return "Favorite"
    return "Boring"
Input = input("Enter a word for Sue: ").lower()
result = check_word_for_sue(Input)
print(result)
print("\nQuestion 5\n")
def check_factory_weights():
    print("Enter the package weights (type 'done' when finished):")
    weights = []

    while True:
        entry = input("Weight: ").lower()
        if entry == 'done':
            break
        try:
            weights.append(float(entry))
        except ValueError:
            print("Please enter a valid number.")

    if not weights:
        print("No packages weighed.")
        return
        
    first_weight = weights[0]
    is_consistent = all(w == first_weight for w in weights)

    if is_consistent:
        print("Pass")
    else:
        print("Fail")

check_factory_weights()