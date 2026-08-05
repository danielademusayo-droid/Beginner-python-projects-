import tkinter as tk
from tkinter import messagebox

def submit():
    name = entry.get()
    messagebox.showinfo("Welcome", f"Hello {name}!\nWelcome to FUTA Coding Club 🎉")

# Create the window
root = tk.Tk()
root.title("FUTA Coding Club")
root.geometry("400x300")

tk.Label(root, text="Enter Your Name:", font=("Arial", 14)).pack(pady=20)

entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.pack()

tk.Button(root, text="Submit", font=("Arial", 12), command=submit).pack(pady=20)

root.mainloop()
