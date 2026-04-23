import turtle
import random

"""
Problem 1. Click counter
Create a variable for counting mouse clicks.
Write a program that responds to left mouse clicks as follows:
- Increase the counter by 1.
- Print the value of the counter in the Console.
"""
print ("problem 1")
screen = turtle.Screen()
screen.title("Click Counter")

click_count = 0


"""
Problem 2. Click counter 2
Modify the solution from problem 1 so that instead of printing to the Console, the information is written
on the canvas.
"""




"""
Problem 3. Color cycle
Crate a list of colors of your choice. Draw a circle that has the first color from the list.
Make your program respond to mouse clicks as follows:
- Select the next color from the list of colors. If the current color is the last one in the list, go
back to the first color.
- Draw a circle of the selected color. (The location of the circle should not change.)
Tip: you will need a variable that remembers the index of the current color in the list.
Example:
List of colors: [&#39;green&#39;, &#39;red&#39;, &#39;blue&#39;]
At the start of the
program

After the 1 st click After the 2 nd click After the 3 rd click

Reminders:
The code below draws a circle of radius 50:
p = turtle.Pen()
p.circle(50)
How to fill a shape with color:
p.begin_fill()
# draw the shape here
p.end_fill()
"""
print ("problem 3")
screen = turtle.Screen()
screen.title("Color Cycle")

colors = ["green", "red", "blue"]
current_color_index = 0

p = turtle.Pen()
p.circle(50)

def change_color(x, y):
    global current_color_index
    current_color_index = (current_color_index + 1) % len(colors)
    p.clear()
    p.color(colors[current_color_index])
    p.begin_fill()
    p.circle(50)
    p.end_fill()
    p.color("black")
    p.write(f"Color: {colors[current_color_index]}", align="center", font=("Arial", 12, "normal"))
    p.penup()
    p.goto(0, -60)
    p.pendown()
    p.write(f"Clicks: {click_count}", align="center", font=("Arial", 12, "normal"))
    p.penup()
    p.goto(0, 0)
    p.pendown()
    click_count += 1
    print(f"Click count: {click_count}")
    p.write(f"Click count: {click_count}", align="center", font=("Arial", 12, "normal"))
    p.penup()
    p.goto(0, -60)
    p.pendown()
    p.write(f"Clicks: {click_count}", align="center", font=("Arial", 12, "normal"))
    p.penup()
    p.goto(0, 0)
    p.pendown()
    p.write(f"Color: {colors[current_color_index]}", align="center", font=("Arial", 12, "normal"))
    p.penup()
    p.goto(0, -60)
    p.pendown()
    p.write(f"Clicks: {click_count}", align="center", font=("Arial", 12, "normal"))
    p.penup()
    p.goto(0, 0)
    p.pendown()
    p.write(f"Color: {colors[current_color_index]}", align="center", font=("Arial", 12, "normal"))
    p.penup()
    p.goto(0, -60)
    p.pendown()
    p.write(f"Clicks: {click_count}", align="center", font=("Arial", 12, "normal"))
    p.penup()
    p.goto(0, 0)
    p.pendown()
    p.write(f"Color: {colors[current_color_index]}", align="center", font=("Arial", 12, "normal"))
    p.penup()
    p.goto(0, -60)
    p.pendown()
    p.write(f"Clicks: {click_count}", align="center", font=("Arial", 12, "normal"))
    p.penup()
    p.goto(0, 0)
    p.pendown()
    p.write(f"Color: {colors[current_color_index]}", align="center", font=("Arial", 12, "normal"))
    p.penup()
    p.goto(0, -60)
    p.pendown()
    p.write(f"Clicks: {click_count}", align="center", font=("Arial", 12, "normal"))
    p.penup()
    p.goto(0, 0)
  






"""
Problem 4. Concentric circles (challenge)
In this problem you will be drawing 10 concentric circles – circles that have the same
center. The radii of the circles will decrease by 10. The radius of the biggest circle is
100. The radius of the smallest one is 10.
Make your program respond to left mouse clicks as follows:
- Choose a random color.
- Draw a circle. The radius of this circle should be 10 less than the radius of the
circle you drew on the previous click. Unless it was the last one (with radius
10). In this case, you should draw a circle of radius 100.
Tip: you will need a variable that remembers the radius of the current circle.

At the start of theprogram

After the 1 st click After the 2 nd click After the 3 rd click

After the 9 th click After the 10 th click After the 11 th click
"""
print ("problem 4")



"""
Problem 5. Red color (challenge)
In this problem you will be changing the color of the background on click. At the start of the program
set the background color as indicated below:
- Set the red component to 1.
- Set the green and blue components to random values (reminder: they must be floating-point
numbers between 0 and 1; use function random.random()).
Write “New color” on the canvas.
Make your program respond to left mouse clicks as follows:
- Remove the words “new color” from the canvas.
- Reduce the red component by 0.2.
- If the value of red goes below 0, reset it back to 1, set the blue and green components to new
random values, and write “New color” on the canvas again.
"""
print  ("problem 5")  
screen = turtle.Screen()
screen.title("Red Color")
screen.bgcolor(1, random.random(), random.random())
p = turtle.Pen()
p.write("New color", align="center", font=("Arial", 12, "normal"))  
def change_color(x, y):
   r, g, b = screen.bgcolor()
   r -= 0.2
   if r < 0:
       r = 1
       g = random.random()
       b = random.random()
       p.clear()
       p.write("New color", align="center", font=("Arial", 12, "normal"))
   screen.bgcolor(r, g, b)

screen.onclick(change_color)
#screen.mainloop()

"""
Weight inspection
You are a worker at a candy factory. Your job today is to check that all packages of candy
from a box have the same weight. You are given a list of readings from an electronic scale –
package weights. Print &#39;Pass&#39; if all the packages have the same weight and &#39;Fail&#39;
otherwise.
Examples:
same_weight([10, 10, 13, 13])  Fail
same_weight([10, 10, 10, 10, 9])  Fail
same_weight([15, 15, 15])  Pass
"""
print ("weight inspection")
def same_weight(weights):
    if len(set(weights)) == 1:
        print("Pass")
        return True

    print("Fail")
    return False

same_weight([10, 10, 13, 13])
same_weight([10, 10, 10, 10, 9])
same_weight([15, 15, 15])

"""
Number issue
Joe wrote several numbers on the board and said that they are in increasing order
(each number is smaller than the next one). Bob disagrees. Help the boys settle the
issue.
Write a function with 1 parameter: a list of numbers that Joe wrote on the board.
This function should print &#39;Joe&#39; if Joe is right. Otherwise, it should print &#39;Bob&#39;.
Examples:
number_issue([5, 6, 6, 10])  Bob
number_issue([10, 100, 3000])  Joe
number_issue([1, 2, 3, 4, 2])  Bob
Tip: either search or counting algorithms can be used here.
"""
print ("number issue")
def number_issue(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i + 1]:
            print("Bob")
            return False
    print("Joe")
    return True

number_issue([5, 6, 6, 10])
number_issue([10, 100, 3000])
number_issue([1, 2, 3, 4, 2])


"""
Peaks (Challenge)
We will call a value in a list a “peak” if it is bigger than both of its neighbors.
For example, in the list [2, 1, 4, 3] there is 1 “peak” value: 4.
Write a function with 1 parameter: a list of numbers. It should print all the “peak” values in the list and
print how many “peaks” there are in the list.
Examples:
List Output
[10, 20] Number of peaks: 0
[-3, 13, 2, 14] Peak values:

13
Number of peaks: 1
[50, 1, 30, 2, 10, 15, 7] Peak values:

30
15
Number of peaks: 2

"""
print ("peaks")
def peaks(numbers):
   peak_values = []
   for i in range(1, len(numbers) - 1):
       if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
           peak_values.append(numbers[i])
   print("Peak values:")
   for value in peak_values:
       print(value)
   print(f"Number of peaks: {len(peak_values)}")  
  
peaks([10, 20])
peaks([-3, 13, 2, 14])
peaks([50, 1, 30, 2, 10, 15, 7])


