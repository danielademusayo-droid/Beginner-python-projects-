import tkinter as tk
from tkinter import messagebox

# Dictionary to store users (in memory)
users = {}

def register():
    username = username_entry.get().strip()
    password = password_entry.get()
    confirm_password = confirm_entry.get()
    try:
        age = int(age_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid age!")
        return

    if not username or not password:
        messagebox.showerror("Error", "Username and Password cannot be empty!")
        return

    if username in users:
        messagebox.showerror("Error", "Username already exists!")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    if age < 18:
        messagebox.showerror("Error", "You must be 18 or above to register.")
        return

    # Save user
    users[username] = password
    messagebox.showinfo("Success", f"Account created successfully!\nWelcome {username} 🎉")
    
    # Clear fields
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)


def login():
    username = login_username_entry.get().strip()
    password = login_password_entry.get()

    if username in users and users[username] == password:
        messagebox.showinfo("Success", f"Login successful!\nWelcome back, {username} 🎉")
    else:
        messagebox.showerror("Error", "Invalid username or password!")


# ==================== Main Window ====================
root = tk.Tk()
root.title("FUTA Coding Club")
root.geometry("500x600")
root.resizable(False, False)

# Title
tk.Label(root, text="FUTA Coding Club", font=("Arial", 18, "bold")).pack(pady=20)

# ===================== REGISTER SECTION =====================
tk.Label(root, text="Register New Account", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(pady=5)

tk.Label(root, text="Confirm Password:").pack()
confirm_entry = tk.Entry(root, width=30, show="*")
confirm_entry.pack(pady=5)

tk.Label(root, text="Age:").pack()
age_entry = tk.Entry(root, width=30)
age_entry.pack(pady=5)

tk.Button(root, text="Register", bg="green", fg="white", font=("Arial", 12), command=register).pack(pady=15)

# ===================== LOGIN SECTION =====================
tk.Label(root, text="Already have an account? Login", font=("Arial", 14, "bold")).pack(pady=20)

tk.Label(root, text="Username:").pack()
login_username_entry = tk.Entry(root, width=30)
login_username_entry.pack(pady=5)

tk.Label(root, text="Password:").pack()
login_password_entry = tk.Entry(root, width=30, show="*")
login_password_entry.pack(pady=5)

tk.Button(root, text="Login", bg="blue", fg="white", font=("Arial", 12), command=login).pack(pady=15)

root.mainloop()
