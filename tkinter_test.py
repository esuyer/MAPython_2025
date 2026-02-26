import tkinter as tk

def on_click():
    label.config(text="Hello, Tkinter!")

root = tk.Tk()
root.title("Tkinter Test")

label = tk.Label(root, text="Welcome to Python Tkinter")
label.pack(pady=10)

button = tk.Button(root, text="Click Me", command=on_click)
button.pack(pady=5)

print("Starting Tkinter window...")
# Note: In a headless environment, this might not show a window
# but it confirms the library is available and working.
# root.mainloop()
print("Tkinter is configured correctly!")
