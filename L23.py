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
screen.mainloop()



