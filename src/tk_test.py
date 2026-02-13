import os
import turtle
import tkinter as tk

print("Testing Tkinter and Turtle support...")

# Tkinter test
try:
    root = tk.Tk()
    root.title("Tkinter Test")
    label = tk.Label(root, text="Tkinter is working!")
    label.pack()
    root.after(2000, root.destroy) # Auto close after 2 seconds
    root.mainloop()
    print("Tkinter test: SUCCESS")
except Exception as e:
    print(f"Tkinter test: FAILED - {e}")

# Turtle test
try:
    screen = turtle.Screen()
    screen.title("Turtle Test")
    t = turtle.Turtle()
    t.forward(100)
    t.right(90)
    t.forward(100)
    print("Turtle test: SUCCESS")
    screen.exitonclick()
except Exception as e:
    print(f"Turtle test: FAILED - {e}")
