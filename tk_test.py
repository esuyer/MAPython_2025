import tkinter as tk

root = tk.Tk()
root.title("Tkinter Test")
root.geometry("300x200")

label = tk.Label(root, text="Tkinter is working!", font=("Arial", 14))
label.pack(expand=True)

button = tk.Button(root, text="Close", command=root.destroy)
button.pack(pady=20)

root.mainloop()
